# 修改PVF ，初始职业转职后，四个一转职业的技能都可以学习   skill
# 需要修改技能树的位置，使每一个职业的技能树都可以展示四个职业的技能  clientonly/skilltree
# 如果标签为 [skill class] 则把值修改为4
# 修改标签 [growtype maximum level] 的每一个值都为当中的最大值


import re
import os


# 获取每一个标签的名称
def get_lable(line):
    reg = re.match('\[/?(\w+( \w+)*)\]', line)
    if reg:
        return reg[1].lower()
    else:
        return None


# 处理技能文件
# 使skill class标签为4
# 使growtype maximum level 和 second growtype maximum level 标签的值都为当前的最大值
def edit_skill_pvf():
    skl_file = fileutils.get_file_list("C:\\Users\\Spring\\Desktop\\Script\\")
    for i in skl_file:
        if not i.endswith(".skl"):  # 只处理 .skl 结尾的文件
            continue
        print("开始处理：" + i)
        with open(i, 'r', encoding='UTF-8') as file:
            text = ''
            line = file.readline()
            while line:
                counter1 = 0  # 计数
                counter2 = 0  # 计数
                counter3 = 0  # 计数  用于修改技能所需sp
                tmp_label = get_lable(line)
                if tmp_label == "skill class":
                    counter1 += 1  # 如果标签为 skill class 则+1,目的使修改下一行的值
                    text = text + line
                    line = file.readline()
                # if counter1 == 1:
                #     line = "\t4\n"
                if tmp_label == "growtype maximum level" or tmp_label == "second growtype maximum level":
                    counter2 += 1
                    text = text + line
                    line = file.readline()
                if counter2 == 1:
                    line_list = line.split("\t")
                    len = line_list.__len__()
                    max_value = max(line_list)
                    num = 1
                    temp_line = ""
                    while num < len:
                        temp_line = temp_line + "\t" + max_value.strip("\n")  # 有些数据自带\n,这里不需要,所以去除
                        num += 1
                        if num == len:
                            temp_line = temp_line + "\n"
                    line = temp_line

                text = text + line
                line = file.readline()
        file = open(i, 'w', encoding='utf-8')
        file.write(text)
        print("处理完成：" + i)


# 获取技能位置
def get_position(line):
    reg = re.match('(\t)+(\d)+\t(\d)+', line)
    if reg:
        return line
    else:
        return None


# 修改技能树
def edit_skilltree_pvf():
    co_file = fileutils.get_file_list("C:\\Users\\Spring\\Desktop\\Script\\clientonly\\skilltree")
    for i in co_file:
        file_name = os.path.basename(i)
        if (file_name == "creator_sp.co"  # 这些不做处理 宠物)
                or file_name == "demonicswordman_sp.co"  # 黑暗武士
                # or file_name=="thief_sp.co"     # 暗夜刺客
                # or file_name=="thief_tp.co"
                # or file_name=="atmage_sp.co"    # 男魔法师
                # or file_name == "atmage_tp.co"
        ):
            continue
        print("开始处理：" + i)
        with open(i, 'r', encoding='UTF-8') as file:
            text = ""  # 转职前技能位置描述
            text2 = ""  # 转职后技能位置描述
            line = file.readline()
            caree_dict = {}  # 职业字典,文件中包含的职业
            counter1 = 0  # 计数
            while line:
                if "`" in line:
                    counter1 += 1
                    caree_dict[counter1] = line
                if counter1 <= 2:
                    text = text + line
                position = get_position(line)  # 匹配位置,并返回位置数据
                if position and counter1 > 2:
                    position_list = position.split("\t")
                    position_x = position_list[3]
                    position_y = position_list[4]  # 因为前面有3个\t，下标4为第二个数字
                    if counter1 == 6:
                        if i.endswith("_sp.co"):   # sp技能
                            position_y = int(position_y) + 1000
                        elif(i.endswith("_tp.co")): # tp特性技能
                            position_y = int(position_y) + 200
                    if counter1 == 8:
                        if i.endswith("_sp.co"):   # sp技能
                            position_y = int(position_y) + 2000
                        elif(i.endswith("_tp.co")): # tp特性技能
                            position_y = int(position_y) + 400
                    if counter1 == 10:
                        if i.endswith("_sp.co"):   # sp技能
                            position_y = int(position_y) + 3000
                        elif(i.endswith("_tp.co")): # tp特性技能
                            position_y = int(position_y) + 600
                    line = "\t\t\t" + str(position_x) + "\t" + str(position_y).rstrip("\n") + "\n"
                    text2 = text2 + line
                    line = file.readline()
                    continue
                if counter1 > 2 and (not "`" in line and not "character job" in line):
                    text2 = text2 + line
                line = file.readline()
        lable = '''[/character job]

[character job]\n'''
        lable1 = '''[/character job]\n'''

        max_num = max(caree_dict.keys())
        file_data=""
        if max_num == 10:  # 可转职4个职业时
            file_data = text + caree_dict[3] + caree_dict[4] + text2 + lable \
                        + caree_dict[5] + caree_dict[6] + text2 + lable \
                        + caree_dict[7] + caree_dict[8] + text2 + lable \
                        + caree_dict[9] + caree_dict[10] + text2 + lable1
        if max_num == 6:  # 可转职2个职业时
            file_data = text + caree_dict[3] + caree_dict[4] + text2 + lable \
                        + caree_dict[5] + caree_dict[6] + text2 + lable1

        file = open(i, 'w', encoding='utf-8')
        file.write(file_data)
        print(file_data)
        print("处理完成：" + i)


if '__main__' == __name__:
    edit_skilltree_pvf()
