from flask import Flask
from flask import request
from flask import render_template
from janome.tokenizer import Tokenizer

app = Flask(__name__)
t = Tokenizer()

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

@app.route("/sample_res")
def sample_res():
    text = request.args.get("msg", "Not defined")
    return text

@app.route('/janome')
def janome(name=None):
    tokens = t.tokenize('分かち書きモードがつきました！',wakati=True)
    res = ""
    for token in tokens:
        res += token
        res += " "
    return res

@app.route('/janome2')
def janome2(name=None):
    text = request.args.get("msg", "Not defined")
    sep = request.args.get("sep", " ")
    tokens = t.tokenize(text, wakati=True)
    res = ""
    for token in tokens:
        res += token
        res += sep
    return res

if __name__ == '__main__':
    app.run()
