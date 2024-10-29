from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False
app.app_context().push() 

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def root():
    """homepage """
    pets = Pet.query.filter(Pet.available == True).limit(10).all()
    return render_template('home.html', pets=pets)




@app.route('/add', methods=['GET', 'POST'])
def add_new_pet():
    """reders the new pet form + handles submission"""

    form = AddPetForm()
    if form.validate_on_submit():
        pet = Pet(name = form.name.data,
                  species = form.species.data,
                  photo_url = form.photo_url.data,
                  age = form.age.data,
                  note = form.note.data,)
        db.session.add(pet)
        db.session.commit()

        return redirect('/')
    else:
        return render_template('add_form.html', form=form)
    
@app.route('/<int:pet_id>')
def get_pet_profile(pet_id):
    """display the pet profile"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    return render_template('profile.html', pet=pet, form=form)

@app.route('/<int:pet_id>', methods=['POST'])
def edit_pet_profile(pet_id):
    """edit the pet profile"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.note = form.note.data
        if form.adopted.data:
            pet.available = False
        else:
            pet.availble = True
        db.session.commit()
        return redirect('/')
    else:
        return render_template('profile.html', form=form, pet=pet)



    
