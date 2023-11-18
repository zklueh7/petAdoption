from flask import Flask, render_template, flash, redirect, render_template
from models import db, connect_db, Pet

from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.app_context().push()

app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_adoption"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

connect_db(app)
db.create_all()

@app.route('/')
def homepage():
    """Home page"""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def show_add_pet_form():
    """Show add pet form"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        newPet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(newPet)
        db.session.commit()
        flash(f"Added {name}!")
        return redirect("/add")
    else:
        return render_template('add_pet_form.html', form=form)

@app.route('/<pet_id>', methods=["GET", "POST"])
def show_pet_detail(pet_id):
    """Show details and edit form for pet"""
    form = EditPetForm()
    pet = Pet.query.get(pet_id)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"Updated {pet.name}!")
        return redirect(f"/{pet.id}")
    else:
        return render_template('pet_detail.html', pet=pet, form=form)