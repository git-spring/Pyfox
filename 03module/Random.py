# random  生成随机数

import random

# 生成[0,1)之间的随机浮点数
random.random()
# 生成指定数之间的随机浮点数
random.uniform(1,10)
# 生成指定数之间的随机整数
random.randint(10,100)
# 生成指定数之间的随机整数,可以指定步长
random.randrange(0,100,3)

# 从序列中获取一个随机元素
random.choices(range(9))  # 返回列表
random.choice(range(9))   # 返回元素

# 把列表中的元素随机排序(洗牌),不生成新的对象
nums = [1,2,3,4,5,6,7,8]
random.shuffle(nums)

