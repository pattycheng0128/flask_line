from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/variable')
def variable():
    employee = {'number':'1234', 'name':'lula', 'gender':'女'}
    hobby = ['jogging', 'play basketball', 'climb mountains']
    return render_template('variable.html', **locals())
    
if __name__ == '__main__':
    app.run()