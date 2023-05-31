import re
import os
import os.path


def funcGetLable(line):
    reg = re.match('\[/?(\w+( \w+)*)\]', line)
    if reg:
        return reg[1].lower()
    else:
        return None


def editequpvf(path):
    raritydroprate = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 200
    }
    template_creationrate = '''[creation rate]
\t%s

[usable job]'''

    with open(path, 'r', encoding='UTF-8') as equfile:
        label = ''
        filedata = ''
        rarity = 0
        skip = False
        find_creationrate = False
        line = equfile.readline()
        while line:
            if not line.strip():
                lastcreationrate = False
                filedata = filedata + line
                line = equfile.readline()
                continue
            tmpLabel = funcGetLable(line)
            if tmpLabel:
                if lastcreationrate:
                    lastcreationrate = False
                    line = '\n%s' % line
                label = tmpLabel
                islabel = True
            else:
                islabel = False
            if islabel:
                if label == 'name':
                    # line = line.replace('(古老) ', '')
                    pass
                elif label == 'rarity':
                    filedata = filedata + line
                    line = equfile.readline()
                    idx = int(line.strip())
                    if idx < 5:
                        rarity = raritydroprate[idx]
                    else:
                        skip = True
                        break
                elif label == 'creation rate':
                    filedata = filedata + line
                    find_creationrate = True
                    line = equfile.readline()
                    if (int(line.strip()) > 0 and int(line.strip()) < rarity):
                        line = str('\t%s\n' % rarity)
                    else:
                        line = str('\t%s\n' % line.strip())
                    lastcreationrate = True
            filedata = filedata + line
            line = equfile.readline()
        if not find_creationrate:
            filedata = filedata.replace('[usable job]', template_creationrate % rarity)

    if not skip:
        print(filedata)
        file = open(path, 'w', encoding='utf-8')
        file.write(filedata)
        file.close()


# 读取装备列表
def readEquipmentList():
    file_name = 'Script/stackable.lst'
    path_prefix = 'Script/stackable/'
    continueuntil = False
    skip = False
    with open(file_name) as file_obj:
        id = file_obj.readline().replace('\n', '')
        path = path_prefix + file_obj.readline().replace('`', '').replace('\n', '')
        while id and path:
            skip = False

            if path.find('avatar') > -1 or path.find('at_avatar') > -1:  # avatar 时装 character 人物(非宠物)  不需要修改
                skip = True
            if not os.path.exists(path) or continueuntil or skip:
                id = file_obj.readline().replace('\n', '')
                path = path_prefix + file_obj.readline().replace('`', '').replace('\n', '')
                continue
            print('dealing----%s %s' % (id, path))
            editequpvf(path)
            id = file_obj.readline().replace('\n', '')
            path = path_prefix + file_obj.readline().replace('`', '').replace('\n', '')


if '__main__' == __name__:
    readEquipmentList()
