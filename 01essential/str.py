# python 字符串

# 定义
# 可以使用双引号、单引号、三对单引号、三对双引号
s = 'str'
s = "str"
s = '''str'''
s = """str"""
# 以上四种写法效果一样

# 在字符串前面添加参数
s = r'\t\nstr define'  # r/R 表示字符串的内容为原生字符,\t \n 等会原样输出
s = u'this is a unicode str'  # u/U 表示unicode字符串  如果内容为中文，需要指定编码
s = b'this is a bytes object'  # b/B 表示这是一个bytes对象
# 在 Python3 中，bytes 和 str 的互相转换方式是str.encode('utf-8')/# bytes.decode('utf-8')

# f/F 表示在字符串内支持大括号内的python 表达式
name = 'liu'
age = '25'
print(f'姓名: {name},age: {age}')  # 输出: 姓名: liu,age: 25

# 字符串的索引  python 中的字符串可以使用索引获取每个位置的字符
s = 'abcde'
for idx in range(len(s)):
    # print(s[idx])
    pass
# 字符串的切片 从原有的字符中复制一段内容
s = 'abcdefghijk'
s1 = s[1:5]
s1 = s[1:2]
s1 = s[:5:3]
s1 = s[3:]
s1 = s[7:2:-1]
print(s1)

## 字符串常见操作
# 查找指定字符串的索引
s = 'str show'
len(s)  # 字符串的长度
idx = s.find('p')  # 查找指定字符在字符串中最先(lowest)出现的索引，如果不存在则返回-1
# idx = str_a.index('p')  # 查找指定字符在字符串中最先(lowest)出现的索引，如果不存在则 报错  ValueError: substring not found
# s.rfind()  # 最后(highest)出现的索引  如果不存在则返回-1
# s.rindex() # 最后(highest)出现的索引  如果不存在则 报错  ValueError: substring not found
print(idx)
print(s.count('e'))

# 判断开头/结束
s = 'judgement str'
idx = s.index('m')
b = s.startswith('ju')  # 是否以 ju 开头
b = s.endswith('ent')  # 是否以 ent 结束
print('abcdef'.isalpha())  # 字符串的内容是否全是字母
print('123'.isdigit())  # 是否是数字
print('1.5'.isnumeric())  #
print('123abc'.isalnum())  # 是否由数字和字母组成
print('     '.isspace())  # 是否由空格组成
print('ABC'.isupper())
print('abc'.islower())
...

# 字符串替换
word = 'foot'
new_word = word.replace('oo', 'ee')
print(new_word)

# 字符串分割
s = '2020-11-18'
split = s.split('-')  # 分割后的元素组成一个列表
rsplit = s.rsplit('-', 1)  # ['2020-11', '18']

# partition  指定一个字符为分隔符，把字符分为三个部分 (前一部分 分隔符 后一部分)
s = 'abcdXqwXer'
part = s.partition('X')  # ('abcd', 'X', 'qwer')   以第一个匹配的字符为分隔符
part = s.rpartition('X')  # ('abcdXqw', 'X', 'er')  以最后一个匹配字符为分隔符

# 查看字符对应的编码
print(ord('a'))  # 查看字符对应的asscii码
print(chr(65))  # 查看asscii对应的字符

# format
print('name: %s, age: %d ' % ('lisi', 18))
print('name: {}, age: {}'.format('lisi', 18))
print('name: {0}, age: {1}'.format('lisi', 18))
print('name: {name}, age: {age}'.format(age=18, name='lisi'))
