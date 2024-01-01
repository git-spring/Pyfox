# 人偶

import re


# 获取每一个标签的名称
def get_lable(line):
    reg = re.match('\[/?(\w+( \w+)*)\]', line)
    if reg:
        return reg[1].lower()
    else:
        return None


# 修改人偶的冷却时间和可使用等级
def edit_puppet_pvf():
    skl_file = fileutils.get_file_list("C:\\Users\\Spring\\Desktop\\Script\\stackable\\professional\\puppet\\")
    for i in skl_file:
        print("开始处理：" + i)
        with open(i, 'r', encoding='UTF-8') as file:
            text = ''
            line = file.readline()
            while line:
                counter1 = 0  # 计数
                counter2 = 0  # 计数
                tmp_label = get_lable(line)
                if tmp_label == "minimum level":   # 可使用等级
                    counter1 += 1
                    text = text + line
                    line = file.readline()

                if tmp_label == "cool time" :  # 冷却时间
                    counter2 += 1
                    text = text + line
                    line = file.readline()
                if counter1 == 1:
                    line = "\t10\n"
                if counter2 == 1:
                    line = "\t1000\n"   # 1000ms

                text = text + line
                line = file.readline()
        file = open(i, 'w', encoding='utf-8')
        file.write(text)
        print("处理完成：" + i)


if '__main__' == __name__:
    edit_puppet_pvf()
