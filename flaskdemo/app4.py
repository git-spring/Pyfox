# 把数据传递到模板中

from flask import Flask, request, Response, render_template

app = Flask(__name__)
app.config.from_pyfile('settings.py')


# 通过模板引擎传递数据到模板中
@app.route('/app4/show')
def index():
    full_name = 'lisi'
    age = 25
    customers = ['穆', '襄', '惠', '武']
    return render_template('show.html', name=full_name, age=age, gender='male',
                           customers=customers)  # 在模板中用{{name}} 获取数据


if __name__ == '__main__':
    app.run()

# flask 模板学习
# https://blog.csdn.net/troysps/article/details/80466916
