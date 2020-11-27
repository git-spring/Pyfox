# sort方法 和 sorted函数
# python 中的sort和sorted 都可以用于排序
# sort 是一个方法,只能对可变序列排序,排序后不生成新的序列
# sorted 是一个函数,排序后生成新的序列

def lens(s):
    return len(s)


stack = ['a', 'list', 'lisi', 'zhangsan', 'hive', 'spark', 'flink', 'mysql']
# sort
stack.sort()
stack.sort(reverse=True)  # 可以指定倒序
stack.sort(key=lens, reverse=True)  # key 可以指定按什么排序,接收一个函数
print(stack)

# sorted
stack_new = sorted(stack)
stack_new = sorted(stack, key=lens, reverse=True)
print(stack_new)

# 按列表元素的长度排序
alpha = ['shwa', 'shore', 'show', 'shower', 'shoes', 'shanghai', 'aspire']
alpha.sort(key=len)  # 如果是对元组等不可变序列，只能使用sorted
alpha1 = sorted(alpha, key=len)


# 对字典排序
person = {'name': 'lisi', 'age': 20, 'gender': 'female'}
person1 = sorted(person)  # 默认对字典中的key的ascii进行排序
person1 = sorted(person.items(), key=lambda x: len(x[0]))  # 按照key的长度排序
print(person1)
