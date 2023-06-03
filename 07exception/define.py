# python 中的异常处理


"""
处理异常的格式
    try:
        <语句>        # 正常运行的代码
    except [异常类] [as var]:
        <语句>        # 发生异常时运行的代码 except 可以有多个
    else:
        <语句>        # 如果没有异常发生
    finally:
        <语句>        # 最后运行的语句
"""


def div(a, b):
    return a / b


var = [1, 2, 3, 4, 5, 6, 7]

try:
    x = div(5, 1)
    y = var[10]
except ZeroDivisionError as e:
    print('[ERROR] ------ 除0错误')
except IndexError as e:
    print('[ERROR] ------ 索引越界')
except (ZeroDivisionError, IndexError) as e:  # 可以使用一个元组来捕获多个异常
    pass
else:
    print(x, y)
finally:
    print('最后运行的代码')
