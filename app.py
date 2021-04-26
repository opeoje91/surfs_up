from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/about')
def sho_family():
    return 'Ivana'

@app.route('/fruits')
def fruits():
    name = 'apple, banana'
    return name
