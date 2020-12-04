# python 中的json 模块

import json


"""
python数据类型与json数据类型的映射关系
    Python                  JSON
    dict                    object
    list, tuple	            array
    str, unicode            string
    int, float              number
    True                    true
    False                   false
    None                    null
    
    
json中常用的方法
    方法	              描述
    json.dumps()      将 Python 对象编码成 JSON 字符串
    json.loads()      将已编码的 JSON 字符串解码为 Python 对象
    json.dump()       将Python内置类型序列化为json对象后写入文件
    json.load()       读取文件中json形式的字符串元素转化为Python类型
"""


# dumps
data = {'name':'lisi','age':18}
obj = json.dumps(data)      # {"name": "lisi", "age": 18}  json中字符串默认是双引号

# loads
str = json.loads(obj)
print(str)            # {'name': 'lisi', 'age': 18}
print(type(str))      # <class 'dict'>


# dumps 列表类型
nums = [1,2,3,4,5]
obj = json.dumps(nums)
print(obj)
print(type(obj))

# dump/load  是从文件中操作
data = {
    'acc':'haha',
    'a':[1,2,3,4],
    'b':(1,2,3)
}

with open('../star/json_test.txt', 'w') as f:
    json.dump(data, f)

with open('../star/json_test.txt', 'r') as f:
    print(json.load(f))
