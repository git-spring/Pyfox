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
        0: 200,
        1: 200,
        2: 600,
        3: 400,
        4: 100
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


def readEquipmentList():
    file_name = 'file/list.txt'
    path_prefix = 'file/'
    continueuntil = False
    skip = False
    with open(file_name) as file_obj:
        id = file_obj.readline().replace('\n', '')
        path = path_prefix + file_obj.readline().replace('`', '').replace('\n', '')
        print(path)
        while id and path:
            skip = False
            print('dealing----%s %s' % (id, path))
            if path.find('avatar') > -1:
                skip = True
            if not os.path.exists(path) or continueuntil or skip:
                id = file_obj.readline().replace('\n', '')
                path = path_prefix + file_obj.readline().replace('`', '').replace('\n', '')
                continue
            editequpvf(path)
            id = file_obj.readline().replace('\n', '')
            path = path_prefix + file_obj.readline().replace('`', '').replace('\n', '')


if '__main__' == __name__:
    readEquipmentList()
