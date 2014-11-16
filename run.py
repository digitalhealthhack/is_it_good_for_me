from flask import Flask
from flask import render_template
from flask import request
from flask import json

APP = Flask(__name__)


@APP.route('/')
def index():
    return render_template('index.html')

@APP.route('/diseases',methods=['GET', 'POST'])
def diseases():
    if request.method == 'POST':
        return return_diseases()

    else:
        print "inside else"
        return show_diseases()

def return_diseases():
    diseases = {
        "1": {
        "id": 1,
        "name": "Cancer",
        "levels": [[.6,'+'],[.2,'-'],[.3,'+'],[.4,'-'],[.5,'+']],
        "confidence": .88,
        "title": "Green tea prevents cancer",
        "content": "Because YADSFASDFASDFASDFASDFASDFASYADSFASDFASDFASDFASDFASDFASDYADSFASDFASDFASDFASDFASDFASDYADSFASDFASDFASDFASDFASDFASDYADSFASDFASDFASDFASDFASDFASDD",
        },
        "2":{
        "id": 2,
        "name": "Heart Disease",
        "levels": [[.6,'+'],[.2,'-'],[.3,'+'],[.4,'-'],[.5,'+']],
        "confidence": .88,
        "title": "Green tea prevents hard disease",
        "content": "Because YADSFASDFASDFASDFASDFASDFASYADSFASDFASDFASDFASDFASDFASDYADSFASDFASDFASDFASDFASDFASDYADSFASDFASDFASDFASDFASDFASDYADSFASDFASDFASDFASDFASDFASDD",
        },
        "3":{
        "id": 3,
        "name": "Obesity",
        "levels": [[.6,'+'],[.2,'-'],[.3,'+'],[.4,'-'],[.5,'+']],
        "confidence": .88,
        "title": "Green tea prevents hard disease",
        "content": "Because YADSFASDFASDFASDFASDFASDFASYADSFASDFASDFASDFASDFASDFASDYADSFASDFASDFASDFASDFASDFASDYADSFASDFASDFASDFASDFASDFASDYADSFASDFASDFASDFASDFASDFASDD",
        }}
    return json.jsonify(diseases)

def show_diseases():
    return render_template('show.html')


if __name__ == '__main__':
    APP.run(debug=True)
