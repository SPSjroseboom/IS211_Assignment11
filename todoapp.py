#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
assingnment11 - todoapp.py
Created on Thu Aug 22 18:19:25 2019
@author: SPSjroseboom
"""
# the server should be accessible from http://localhost:5000
# use ctrl+c to stop running console to try again

from flask import Flask, render_template, request, redirect
import re


app = Flask(__name__)

todolist = []


@app.route('/')
def index():
    return render_template('index.html', todolist=todolist)


@app.route('/submit', methods=['POST'])
def submit():
    task = request.form['taskName']
    priority = request.form['taskPriority']
    email = request.form['emailAddress']

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return redirect('/')
    elif not task:
        return redirect('/')
    elif priority == 'Priority Level':
        return redirect('/')
    else:
        todolist.append((task, priority, email))

    print todolist
    return redirect('/')


@app.route('/clearAllTasks', methods=['POST', 'GET'])
def clear():
    del todolist[:]
    return redirect('/')


if __name__ == '__main__':
    app.run()
