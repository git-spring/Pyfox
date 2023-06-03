# 修改技能属性
# 第一个数字表示 几个数字为一组,后面表示不同的属性含义
# 将属性数据复制到skill_attributes.txt 文件中,运行本python 文件

def edit_skill_attribute_pvf(position):
    attribute_file = "E:\\05pythonProject\Pyfox\\funnygames\\pvf\\skill_attribute.txt"
    print("开始处理：" + attribute_file)
    with open(attribute_file, 'r', encoding='UTF-8') as file:
        line = file.readline()
        attr_list = line.split("\t")   # todo 有些前面只有一个制表符
        group_num = attr_list[1]  # 取出第一个数字,前面有2个制表符,所以下标2是第一个数字
        print(group_num)
        new_list = attr_list[2:]  # 将其余的组成一个新的list
        idx = 0
        new_line = ""  # 新的属性
        import math
        while (idx < len(new_list)):
            if idx % int(group_num) == position - 1:
                new_line = new_line + "\t" + str(math.ceil(int(new_list[idx]) * 3))  # 对应位置上执行什么操作
            else:
                new_line = new_line + "\t" + new_list[idx]
            idx += 1
        final_data = "\t\t" + group_num +  new_line
        print(final_data)

        print("处理完成：" + attribute_file)



# 设计一个字典
# "1",("*",2)  第一个位置 乘 2
dict={
    "1",("*",2)
}

if '__main__' == __name__:

    edit_skill_attribute_pvf(4)  # 需要修改第几个位置,就传入数字几
