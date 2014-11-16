from flask import Flask
from flask import render_template
from flask import request
from flask import json


APP = Flask(__name__)


@APP.route('/')
def index():
    return render_template('index.html')


@APP.route('/diseases', methods=['GET', 'POST'])
def diseases():
    if request.method == 'POST':
        response = get_diseases()
    else:
        response = show_diseases()
    return response


def get_diseases():
    with open('diseases.json', 'r') as json_file:
        text = json_file.read()
    pythoned = json.loads(text)
    return json.jsonify(pythoned)


def show_diseases():
    return render_template('show.html')


if __name__ == '__main__':
    APP.run(debug=True)
