# 修改pvf中的文件，增加掉落假紫

import re
import os
import os.path
import sys


def funcGetLable(line):
    reg = re.match('\[/?(\w+( \w+)*)\]', line)
    if reg:
        return reg[1].lower()
    else:
        return None


def editequpvf(path):
    filedata = ''
    raritydroprate = {
        0: 200,
        1: 200,
        2: 600,
        3: 400,
        4: 100
    }
    template_creationrate = '''[creation rate]
    \t%d
    
    [usable job]'''

    with open(path, 'r', encoding='UTF-8') as equfile:
        label = ''
        rarity = 0
        rarityidx = 0
        islabel = False
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
            if not islabel:
                if label == 'name':
                    # line = line.replace('(古老) ', '')
                    pass
                elif label == 'rarity':
                    idx = int(line.strip())
                    if idx < 5:
                        rarity = raritydroprate[idx]
                    else:
                        skip = True
                        break
                elif label == 'creation rate':
                    find_creationrate = True
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
        file = open(path, 'w', encoding='utf-8')
        file.write(filedata)
        file.close()


def readEquipmentList():
    file_name = './Script/equipment.lst'
    path_prefix = './Script/equipment'
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
