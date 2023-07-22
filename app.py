from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
#
app= Flask(__name__)
app.config['SECRET_KEY'] = 'mysectret'

todos = ["learn flask", "setup venv", "Build cool app"]

class TodoForm(FlaskForm):
    todo = StringField("Todo", validators=[DataRequired()])
    submit = SubmitField("Add Todo")

@app.route('/', methods=['GET', 'POST'])
def index():
    template_form = TodoForm(csrf_enabled=False)
    if template_form.validate_on_submit(): 
        todos.append(template_form.todo.data)
        return redirect(url_for('index'))
    return render_template('index.html', todos=todos, template_form=template_form)