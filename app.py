#! /usr/bin/python
# -*- coding: utf-8 -*-
# @Time: 2022.06.15 04:05
# @Author: fyc
# @Software: VScode

from flask import Flask, jsonify, request, render_template, make_response, send_from_directory, redirect, flash
from flask_login import LoginManager, login_required, login_user, logout_user


app = Flask(__name__)
app.config['ENV'] = 'development'  # 添加这一句！！！将环境设置为开发环境


@app.route("/")
def login():
    return render_template('login.html')


@app.route("/main", methods=['POST', 'GET'])
def main():
    return render_template('main.html')


@app.route("/student", methods=['POST', 'GET'])
def student():
    lengeth = 1
    l = [2019217844, 'fyc', '男', '21', '汉',
         '计算机与信息系', '物联网工程', '19-2', '2019-9-1']
    return render_template('index.html', len=lengeth, l=l)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')
