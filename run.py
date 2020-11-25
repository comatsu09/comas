from flask import Flask
from flask import request
from flask import render_template
from janome.tokenizer import Tokenizer

app = Flask(__name__)
t = Tokenizer()

@app.route('/',  methods=["GET"])
def get():
    return render_template('index.html', \
#    title = 'Form Sample(get)', \
    title = 'Janome(get)', \
#    message = '名前を入力して下さい。')
    message = '文章を入力して下さい。')

@app.route('/',  methods=["POST"])
#def janome(name=None):
def janome():
    #text = request.args.get("msg", "Not defined")
    #sep = request.args.get("sep", " ")
    text = request.form['name']
    tokens = t.tokenize(text, wakati=True)
    res = ""
    for token in tokens:
        res += token
#        res += sep
        res += "*"
    #return res

#@app.route('/',  methods=["POST"])
#def post():
#    name = request.form['name']
    return render_template('index.html', \
#    title = 'Form Sample(post)', \
    title = 'Janome(post)', \
#    message = 'こんにちは、{}さん'.format(name))
    message = 'test:{}'.format(res))

if __name__ == '__main__':
    app.run()
