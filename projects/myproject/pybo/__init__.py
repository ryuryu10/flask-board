from flask import Flask
app = Flask(__name__)

'''
set FLASK_ENV=development
set FLASK_ENV=development
flask run
'''

@app.route('/')
def hello_pybo():
    return 'Hello, Pybo!'