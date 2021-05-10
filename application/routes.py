from application import app, db
from application.models import Task_table

@app.route('/')

@app.route('/home')
def home():
    all_tasks = Task_table.query.all()
    output = ""
    for each_task in all_tasks:
        output += str(each_task.task_id) + "/ / / "+ each_task.task_name + " - " + each_task.description + "   /// " + str(each_task.task_status) + "<br>"
    return output

@app.route('/create')
def create():
    task_one = Task_table(task_name = 'Task one', description = "Do task one")
    db.session.add(task_one)
    db.session.commit()
    return f"A task has been added"


@app.route('/complete/<int:id>')
def complete(id):
    task_to_change = Task_table.query.filter_by(task_id = id).first()
    task_to_change.task_status = True
    db.session.commit()
    return f"Task {id} has been completed!"

@app.route('/incomplete/<int:id>')
def incomplete(id):
    task_to_change = Task_table.query.filter_by(task_id = id).first()
    task_to_change.task_status = False
    db.session.commit()
    return f"Task {id} is set as incomplete"

@app.route('/update/<new_description>')
def update(new_description):
    task_to_change_description = Task_table.query.order_by(Task_table.task_id.desc()).first()
    task_to_change_description.description = new_description
    db.session.commit()
    return f"You have changed the description of the most recent task"

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Task_table.query.filter_by(task_id=id).first()
    db.session.delete(task_to_delete)
    db.session.commit()
    return f"Task {id} has been deleted"