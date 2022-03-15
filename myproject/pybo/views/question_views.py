from datetime import datetime
from re import L

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from .. import db
from ..models import Question
from ..forms import QuestionForm, AnswerForm

bp = Blueprint('question', __name__, url_prefix='/quesiton')

@bp.route('/')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/detail/<int:quesiton_id>/')
def detail(qusetion_id):
    form = AnswerForm()
    question = Question.query.get_or_404(qusetion_id)
    return render_template('question/question_deatil.html', question=question, form=form)
                           
@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.sesstion.commit()
        return redirect(url_for('main.index'))
    return render_template('question/question.html', form=form)

