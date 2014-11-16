from flask import Flask
from flask import render_template
from flask import request
from flask import json


APP = Flask(__name__)


@APP.route('/')
def index():
    return render_template('index.html')


@APP.route('/diseases', methods=['POST'])
def diseases():
    search_query = request.form['treatment']
    response = get_diseases(search_query)
    return response


def get_diseases(search_query):
    with open('diseases.json', 'r') as json_file:
        text = json_file.read()
    pythoned = json.loads(text)

    pythoned = pythoned.get(search_query, pythoned['Chocolate'])

    return json.jsonify(pythoned)


if __name__ == '__main__':
    APP.run(debug=True)
