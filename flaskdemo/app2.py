# app.py 与模板的结合使用

from flask import Flask, request, render_template

app = Flask(__name__)


app.config.from_pyfile('settings.py')


@app.route('/app2/register1')
def index1():
    s = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <form action="" method="get">
        <p><input type="text" placeholder="请输入用户名"></p>
        <p><input type="text" placeholder="请输入地址"></p>
        <p><input type="submit" value="提交"></p>
    </form>
</body>
</html>
    """
    return s


# 　使用模板
@app.route('/app2/register2')
def index2():
    # 使用template 模板,templates 文件夹需要和app.py文件同一级目录
    render = render_template('register.html')
    print(render)
    return render


# 获取页面提交的内容
# methods 是显示声明可以请求的方法
@app.route('/app2/register3', methods=['GET', 'POST'])
def index3():
    # 获取页面提交的内容,username和age是html中定义的name
    print(request.args)
    print(request.args.get('username'))
    print(request.args.get('age'))

    # 如果是POST 请求,需要通过form获取页面提交的内容
    print(request.form)
    print(request.form.get('username'))
    print(request.form.get('age'))
    return '提交成功!'


if __name__ == '__main__':
    # 查看路由规则
    print(app.url_map)
    app.run()
