# set 是python 中的集合
# set 是一个无序不重复元素集

# 定义
# s = {}        # 这样定义的是一个空的dict
s = set()  # 定义一个空set
s = set(range(5))  # 把序列转换成set
s = {1, 2, 3, 4}  # 定义一个包含元素的set

animal = {'dog', 'cat', 'tiger'}
# 增加元素
animal.add('二哈')

# 删除元素
animal.pop()  # 随机删除一个元素
animal.remove('二哈')  # 删除指定元素， 如果元素不存在，则会报错

s1 = {'李白', '杜甫', '王昌龄', '张九龄', '王之涣', '高适', '李龟年', '王维', '孟浩然'}
s2 = {'李白', '杜甫', '王昌龄', '张九龄', '贺知章', '韩愈', '柳宗元', '孟浩然'}
# 并集
s3 = s1.union(s2)
s1.update(s2)  # 把 集合s2 合并到s1 不生成新的集合
s3 = s1 | s2

# 交集
s3 = s1.intersection(s2)
s3 = s1 & s2

# 差集
s3 = s1.difference(s2)
s3 = s1 - s2
