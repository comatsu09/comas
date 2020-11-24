from flask import Flask
from flask import request
from flask import render_template
from janome.tokenizer import Tokenizer

app = Flask(__name__)
t = Tokenizer()

@app.route('/',  methods=["GET", "POST"])
def janome2(name=None):
    #text = request.args.get("msg", "Not defined")
    #sep = request.args.get("sep", " ")
    """
    <form action="/" method="POST">
    <input name="text"></input>
    </form>
    """
    tokens = t.tokenize(text, wakati=True)
    res = ""
    for token in tokens:
        res += token
        res += sep
    return res

'''
@app.route('/test', methods=["GET", "POST"])
def odd_even():
    if request.method == "GET":
        return """
        下に整数を入力してください。奇数か偶数か判定します。
        <form action="/test" method="POST">
        <input name="num"></input>
        </from>"""
    else:
        try:
            return """
            {}は{}です！
            <form action="/test" method="POST">
            <input name="num"></input>
            </form>""".format(str(request.form["num"]), ["偶数", "奇数"][int(request.form["num"]) % 2])
        except:
            return """
                有効な数字ではありません！入力しなおしてください。
                <form action="/test" method="POST">
                <input name="num"></input>
                </form>"""
'''

if __name__ == '__main__':
    app.run()
