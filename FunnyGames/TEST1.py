# 修改指定行的数据

import math

# 修改的文件路径
file_path = 'C:\\Users\\Spring\\Desktop\\Script\\monster\\bossmonsterbaseparameter.tbl'
file_path_bak = file_path + '.bak'

with open(file_path, 'r', encoding='utf8') as file_r, open(file_path_bak, 'w', encoding='utf8') as file_w:
    count = 0
    for row in file_r:
        count += 1
        if count % 24 == 6:  # 修改指定行的数据 血量
            row = int(row) * 1.1
            row = str(math.ceil(row)) + '\n'
        if count % 24 == 9 or count % 24 == 11:  # 修改指定行的数据 防御
            row = int(row) * 1.2
            row = str(math.ceil(row)) + '\n'
        if count % 24 == 10 or count % 24 == 8:  # 修改指定行的数据 攻击
            row = int(row) * 1.2
            row = str(math.ceil(row)) + '\n'
        file_w.write(row)