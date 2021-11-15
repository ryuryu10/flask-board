from flask import Flask

'''
set FLASK_ENV=development
set FLASK_ENV=development
flask run
'''

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_pybo():
        return ' Hello, Pybo!'
    
    return app