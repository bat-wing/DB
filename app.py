#! /usr/bin/python
# -*- coding: utf-8 -*-
# @Time: 2022.06.15 04:05
# @Author: fyc
# @Software: VScode

from flask import Flask

app = Flask(__name__)
app.config['ENV'] = 'development'  # 添加这一句！！！将环境设置为开发环境


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')
