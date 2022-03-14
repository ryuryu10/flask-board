from flask import Blueprintprint

bp = Blueprintprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello!!'

@bp.route('/')
def index():
    return 'PYBO'