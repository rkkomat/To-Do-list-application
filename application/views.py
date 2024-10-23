from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Note
from . import db

view_blueprint = Blueprint('views', __name__)

@view_blueprint.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        task = request.form.get('task1')
        new_note = Note(task_col=task)
        db.session.add(new_note)
        db.session.commit()
    
    tasks = Note.query.order_by(Note.date_created.asc()).all()
    return render_template('index.html', tasks=tasks)

@view_blueprint.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    task_to_delete = Note.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect(url_for('views.home'))
    except:
        flash('There was a problem deleting the task', 'error')
        return redirect(url_for('views.home'))

@view_blueprint.route('/edit_task/<int:id>', methods=['POST'])
def edit_task(id):
    task = Note.query.get_or_404(id)
    task.editing = True
    db.session.commit()
    return redirect(url_for('views.home'))

@view_blueprint.route('/update_task/<int:id>', methods=['POST'])
def update_task(id):
    task = Note.query.get_or_404(id)
    task.task_col = request.form['task_col']
    task.editing = False  # turning off edit mode after updating
    db.session.commit()
    return redirect(url_for('views.home'))

@view_blueprint.route('/complete/<int:id>', methods=['POST'])
def complete_task(id):
    task = Note.query.get_or_404(id)
    task.completed = not task.completed  # toggle the completion status
    db.session.commit()
    return redirect(url_for('views.home'))

