from flask import Flask
from flask import request
from flask import render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        username = request.values['username']
        password = request.values['password']
        if username == 'patty' and password == '1234':
            return '歡迎光臨！'
        else:
            return '密碼錯誤'
    return render_template('index.html')

@app.route('/hello/<string:name>')
def hello(name):
    now = datetime.now() 
    return render_template('hello.html', **locals())

if __name__ == '__main__':
    app.run()