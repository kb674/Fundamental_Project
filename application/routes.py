from application import app, db
from application.models import Task_table, Boarders, Tricks
from application.forms import TaskForm, TrickForm
from flask import render_template, request, redirect, url_for

@app.route('/')

@app.route('/home')
def home():
    all_boarders = Boarders.query.all()
    output = ""
    return render_template("index.html", title="Home", all_boarders=all_boarders)

@app.route('/boarder_view')
def boarder_view():
    all_boarders = Boarders.query.all()
    output = ""
    for each_boarder in all_boarders:
        output += str(each_boarder.boarder_id) + " |    "+ each_boarder.boarder_name + "<br>"
    return output

@app.route('/create', methods=["GET", "POST"])
def create():
    form = TaskForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_boarder = Boarders(boarder_name=form.boarder_name.data)
            db.session.add(new_boarder)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("add_boarder.html", title="Add boarder",form=form)
    

@app.route('/update/<int:id>', methods=["GET","POST"])
def update(id):
    form = TaskForm()
    boarder_name_change = Boarders.query.filter_by(boarder_id = id).first()
    if request.method == "POST":
        boarder_name_change.boarder_name = form.boarder_name.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("update_boarder.html", form=form, title="Update boarder", boarder=boarder_name_change)

@app.route('/delete/<int:id>', methods=["GET","POST"])
def delete(id):
    boarder_delete = Boarders.query.filter_by(boarder_id=id).first()
    db.session.delete(boarder_delete)
    db.session.commit()
    return redirect(url_for("home"))




@app.route('/trick_view')
def trick_view():
    all_tricks = Tricks.query.all()
    output = ""
    for each_trick in all_tricks:
        output += str(each_trick.trick_id) + " |    "+ each_trick.trick_name + " - " + str(each_trick.fk_boarder_id) + "<br>"
    return output


@app.route('/trick_create', methods=["GET", "POST"])
def trick_create():
    form = TrickForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_trick = Tricks(trick_name=form.trick_name.data, fk_boarder_id=form.fk_boarder_id.data)
            db.session.add(new_trick)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("add_trick.html", title="Add trick", form=form)


@app.route('/trick_update/<int:id>', methods=["GET", "POST"])
def trick_update(id):
    form = TrickForm()
    trick_name_change = Tricks.query.filter_by(trick_id = id).first()
    if request.method == "POST":
        trick_name_change.trick_name = form.trick_name.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("update_trick.html", form=form, title="Update trick", trick=trick_name_change)


@app.route('/trick_delete/<int:id>', methods=["GET", "POST"])
def trick_delete(id):
    trick_delete = Tricks.query.filter_by(trick_id=id).first()
    db.session.delete(trick_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route('/assign_trick_to_owner/<int:id>')
def assign_trick_to_owner(id):
    trick_assign = Tricks.query.filter_by(trick_id=id).first()
    trick_assign.fk_boarder_id = 2
    db.session.commit()
    return f"Trick {id} has been assigned to boarder {trick_assign.fk_boarder_id}"
