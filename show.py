from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/show')
def show():
    person1 = {"name":"lulu", "phone": "0922-111-222", "age":"22"}
    person2 = {"name":"lala", "phone": "0933-111-222", "age":"28"}
    person3 = {"name":"yoyo", "phone": "0944-111-222", "age":"33"}
    persons = [person1, person2, person3]
    return render_template("show.html", **locals())

if __name__ == '__main__':
    app.run()