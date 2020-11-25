# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def post():
    name = request.form.get('name')

if __name__ == '__main__':
    app.run()
