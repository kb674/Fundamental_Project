from application import app, db
from application.models import Task_table, Tricks

@app.route('/')

@app.route('/home')
def home():
    all_tricks = Tricks.query.all()
    output = ""
    for each_trick in all_tricks:
        output += str(each_trick.trick_id) + "/   / "+ each_trick.name + " - " + str(each_trick.longboard) + "<br>"
    return output

@app.route('/create')
def create():
    new_trick = Tricks(name = 'cross step')
    db.session.add(new_trick)
    db.session.commit()
    return f"A new trick has been added"


@app.route('/longboard/<int:id>')
def longboard(id):
    trick_change = Tricks.query.filter_by(trick_id = id).first()
    trick_change.longboard = True
    db.session.commit()
    return f"Trick {id} has been categorised as a longboard trick!"

@app.route('/not_longboard/<int:id>')
def not_longboard(id):
    trick_to_change = Tricks.query.filter_by(trick_id = id).first()
    trick_to_change.longboard = False
    db.session.commit()
    return f"Trick {id} has been removed from the longboard list."

@app.route('/update/<new_name>')
def update(new_name):
    trick_change = Tricks.query.order_by(Tricks.trick_id.desc()).first()
    trick_change.name = new_name
    db.session.commit()
    return f"You have changed the name of the most recent trick"

@app.route('/delete/<int:id>')
def delete(id):
    trick_to_delete = Tricks.query.filter_by(trick_id=id).first()
    db.session.delete(trick_to_delete)
    db.session.commit()
    return f"Trick {id} has been deleted"