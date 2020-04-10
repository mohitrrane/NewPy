# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 09:14:10 2020

@author: Mohit Rane
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run()