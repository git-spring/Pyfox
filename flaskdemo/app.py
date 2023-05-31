# flask 的简单使用
# 使用配置变量,引入配置环境
# url路径中加入参数

from flask import Flask, Response

from flaskdemo import settings

app = Flask(__name__)
print(__name__)

# 查看当前的配置
print(app.config)

# 配置单个属性
# app.config['ENV'] = 'development'
# app.config['DEBUG'] = True

# 导入配置文件
app.config.from_object(settings)


# app.config.from_pyfile('settings.py')

# 这些函数称为视图函数
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test/')
def test():
    return '<font color="blue">test world!</font>'


# url中可以带参数,默认是字符串类型
@app.route('/test1/<param>')
def test1(param):
    print(type(param))
    s = 'this is test1 ,这个路由的参数为 %s' % param
    return s


# 指定url中的类型为int,float,uuid,path
@app.route('/test2/<int:param>')
def test2(param):
    print(type(param))
    s = 'this is test2 ,这个路由的参数为 %s' % param
    return s


# 指定url中的类型为path  可以传递 类似 /0/lisi/18 这种形式
@app.route('/test3/<path:param>')
def test3(param):
    print(type(param))
    s = 'this is test3 ,这个路由的参数形式为:<path> 参数为 %s' % param
    return s


@app.route('/test4/')
def test4():
    s = {'name': 'lisi', 'age': 20, 'district': 'lh'}
    return s


if __name__ == '__main__':
    app.run()
