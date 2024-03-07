from flask import Flask, request, render_template,  redirect, flash, session, url_for
from flask_wtf import FlaskForm
#from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  =  False
app.config['SQLALCHEMY_ECHO'] =  True
app.config['SECRET_KEY'] = "chickenzarecool21837"
#app.config['DEBUG_TB_INTERCEPcT_REDIRECTS'] = False
#debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def list_pets():
    """Shows list of all pets in db"""
    pets = Pet.query.all()
    return render_template('list.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        # Create a new pet instance and add it to the database
        new_pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            notes=form.notes.data,
            available=form.available.data
        )
        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')  # Redirect to the homepage after adding a pet
    else:
        return render_template('add_pet.html', form=form)

@app.route("/<int:pet_id>")
def show_pet(pet_id):
    """Show info on a single pet."""

    pet = Pet.query.get_or_404(pet_id)
    return render_template("/list_pet.html", pet=pet)


@app.route('/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """Shows information about a specific pet and allows editing."""
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)
    #video has department here

    if form.is_submitted() and request.method == 'POST':
        # Update the pet instance with the form data and commit the changes to the database
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        flash('Pet updated successfully', 'success')
        return redirect('/')

    return render_template('edit_pet.html', form=form, pet=pet)


