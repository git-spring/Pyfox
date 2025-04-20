# 统计装备的品级和等级，类型

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
        1: 50,
        2: 300,
        3: 400,
        4: 500
    }
    template_creationrate = '''[creation rate]
\t%s

[usable job]'''
    text111 = ""
    with open(path, 'r', encoding='UTF-8') as equfile:
        label = ''
        filedata = ''
        rarity = 0
        skip = False
        find_creationrate = False
        lastcreationrate = False
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
                if label == 'minimum level':
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
                    pass
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
    file_name = 'C:\\Users\\Spring\\Desktop\\Script\\equipment\\equipment.lst'
    path_prefix = 'C:\\Users\\Spring\\Desktop\\Script\\equipment\\'
    continueuntil = False

    with open(file_name) as file_obj:
        id = file_obj.readline().replace('\n', '')  # 装备代码
        path = path_prefix + file_obj.readline().replace('`', '').replace('\n', '')  # 装备路径
        while id and path:  # 当装备代码和装备路径都存在时,循环处理
            skip = False  # 默认不跳过
            if id == '#PVF_File':  # 文件第一行,不需要处理
                skip = True
            print(path)
            if path.find('avatar') > -1 or path.find('creature') > -1:  # avatar 时装 ,宠物  不需要修改
                skip = True
            if not os.path.exists(path) or continueuntil or skip:  # 当装备不存在或者不需要处理时, 继续读取下一个装备的代码和路径
                id = file_obj.readline().replace('\n', '')
                path = path_prefix + file_obj.readline().replace('`', '').replace('\n', '')
                continue
            print('dealing----%s %s' % (id, path))
            editequpvf(path)
            id = file_obj.readline().replace('\n', '')  # 完成处理后,继续读取下一个装备的代码和路径
            path = path_prefix + file_obj.readline().replace('`', '').replace('\n', '')



if '__main__' == __name__:
    readEquipmentList()
