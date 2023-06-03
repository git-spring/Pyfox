# 重定向  status_code 3**
# url_for

from flask import Flask, render_template, request, Response, url_for
from werkzeug.utils import redirect

app = Flask(__name__)  # type:Flask


app.config.from_pyfile('settings.py')

users = []


#
@app.route('/app3/redirect', methods=['post', 'get'])
def index1():
    username = request.form.get('username')
    password = request.form.get('password')
    repassword = request.form.get('repassword')
    if username is not None:
        if password == repassword:
            return redirect('/app3/redirect1')  # 重定向到指定的url路径
    return render_template('index.html')


@app.route('/app3/redirect1', methods=['post', 'get'])
def index2():
    url = request.full_path
    return '注册成功!'


# url_for 路径反向解析
@app.route('/app3/redirect3', methods=['post', 'get'])
def index3():
    url = url_for('url_tag')  # 会找到endpoint 为 url_tag 的视图函数的url
    print(url)
    return redirect(url)  # 重定向


@app.route('/app3/url_for', methods=['post', 'get'], endpoint='url_tag')
def index4():
    return 'url_for() 会把一个标签和url进行映射, 查找标签就会找到对应的url'


if __name__ == '__main__':
    print(app.url_map)
    app.run()
