# 操作文件的工具模块

import os

# 使用递归获取指定目录下的全部文件
def get_file_list(path):
    file_list = []
    for file_name in os.listdir(path):
        full_path = os.path.join(path, file_name)
        if os.path.isfile(full_path):
            file_list.append(full_path)
        elif os.path.isdir(full_path):
            file_list.extend(get_file_list(full_path))
    return file_list

def tolower():
    path="D:\\code\\Pyfox\\"
    file_list = get_file_list(path)
    print(file_list)
    for i in file_list:
        if i.lower().endswith(".py"):
            base_name = os.path.basename(i)
            directory = os.path.dirname(i)
            new_name = directory+"\\"+base_name.lower()
            print(new_name)
            os.rename(i,new_name)

if __name__ == '__main__':
    pass