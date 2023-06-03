# 自定义异常
# 用户自定义异常类型，只要该类继承了Exception类即可，类的内容用户可以自定义


class TooLongExceptin(Exception):
    "this is user's Exception for check the length of name "

    def __init__(self, leng):
        self.leng = leng

    def __str__(self):
        print("[ERROR] --- 姓名长度是" + str(self.leng) + "，超过长度了")


def test(name):
    try:
        if len(name) > 4:
            print('名字长度不符合要求')
            raise TooLongExceptin(len(name))
        print('用户输入的名字是 %s' % name)
    except TooLongExceptin as e:
        e.__str__()


test('liaaa')
