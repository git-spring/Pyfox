# flask 响应对象
# 视图函数返回数据时,都是经过Response 对象返回的

from flask import Flask, Response, make_response, request
import json
app = Flask(__name__)

# 导入配置文件
app.config.from_pyfile('settings.py')


# 使用Response 对象
@app.route('/app1/test1')
def test1():
    return Response('<h2> 所有的东西都会封装成Response 对象返回</h2>')


# 返回一个元组,底层会自动封装成一个Response 对象
@app.route('/app1/test2/')
def test2():
    """
    def __init__(
        self,
        response=None,
        status=None,
        headers=None,
        mimetype=None,
        content_type=None,
        direct_passthrough=False,
    ):
    """
    s = 'response content'
    response = make_response('测试响应头')
    # 响应头中添加内容
    response.headers['mytest'] = 'headers'
    return s, 404


# 获取响应中的内容
@app.route('/app1/test3')
def test3():
    response = Response('获取Response 对象信息')
    print(response.content_type)
    print(response.headers)
    print(response.status_code)
    print(response.status)
    return response


@app.route('/app1/test4')
def test4():
    print(request.headers)
    print(request.path)
    print(request.base_url)
    print(request.url)

    return '获取request 对象信息'


if __name__ == '__main__':
    app.run()
