from flask import Blueprint, render_template
from pybo.models import Question
from ..forms import QuestionForm

bp = Blueprint('question', __name__, url_prefix='/quesiton')

@bp.route('/')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/detail/<int:quesiton_id>/')
def detail(qusetion_id):
    question = Question.query.get_or_404(qusetion_id)
    return render_template('question/question_deatil.html', question=question)
                           
@bp.route('/create/')
def create():
    form = QuestionForm()
    return render_template('question/question.html', form=form)