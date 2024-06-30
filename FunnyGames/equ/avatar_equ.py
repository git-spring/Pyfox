# 处理时装
# 修改时装的最小穿戴等级


import re
import utils.file_utils as fileUtils


# 获取每一个标签的名称
def get_lable(line):
    reg = re.match('\[?(\w+( \w+)*)\]', line)  # '\[/?(\w+( \w+)*)\]'
    if reg:
        return reg[1].lower()
    else:
        return None



def edit_avatar_equ():
    skl_file = fileUtils.get_file_list("C:\\Users\\Spring\\Desktop\\Script\\equipment\\character\\")
    for i in skl_file:
        if not ("avatar") in i or not i.endswith(".equ") :  # 只处理路径包含 avatar 的equ文件
            continue
        print("开始处理：" + i)
        with open(i, 'r', encoding='UTF-8') as file:
            text = ''
            line = file.readline()
            while line:
                counter1 = 0  # 计数
                tmp_label = get_lable(line)
                if tmp_label == "minimum level":
                    counter1 += 1  # 如果标签为 minimum level 则+1,目的是修改下一行的值
                    text = text + line
                    line = file.readline()
                if counter1 == 1:
                    val = int(line.strip("\t"))
                    if val > 5:   # 如果大于5,则改成5,否则保持不变
                        line = "\t5\n"
                text = text + line
                line = file.readline()
        file = open(i, 'w', encoding='utf-8')
        file.write(text)
        # print("处理完成：" + i)






if '__main__' == __name__:
    # 写入原文件,不可重复运行
    edit_avatar_equ()
