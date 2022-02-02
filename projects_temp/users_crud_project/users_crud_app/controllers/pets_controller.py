from users_crud_app import app
## here we are importing the app created in __init__.py
from flask import render_template, redirect, request
## since we imported the app from __init__.py, when we say from flask, we dont need to import Flask as it was already imported on the __init__.py file. we can just import what routing types we will use.
from users_crud_app.models.pet import Pet
## here we are importing the class instance of pet to created routes for pet class. 
from users_crud_app.models.user import User
# from users_crud_app.models import pet
# from users_crud_app.models import user

@app.route('/pets')
def pet_dashboard():
    pets = Pet.get_all()
    return render_template('pets_dash.html', pets=pets)

@app.route('/pets/new')
def pet_new():
    
    users = User.get_all()
    return render_template('pets_new.html', users=users)

@app.route('/pets/create', methods=['POST'])
def pet_create():
    data = {
        'name' : request.form['name'],
        'type' : request.form['type'],
        'user_id' : request.form['user_id']
    }
    #NOTE: look at users_controller to see how I did the same thing but in less code. 
    Pet.save(data)
    return redirect('/pets')

@app.route('/pets/<int:pet_id>')
def display_pet(pet_id):
    
    pet = Pet.show_pet(pet_id)
    return render_template('show_pet.html', pet=pet)

@app.route('/pets/<int:pet_id>/edit')
def edit_pet_page(pet_id):
    users = User.get_all()
    pet = Pet.show_pet(pet_id)
    return render_template('pet_edit.html', pet=pet, users=users)

## this currently is just redirecting. its not updating. 
@app.route('/pets/<int:pet_id>/update', methods = ['POST'])
def update_pet(pet_id):
    User.get_all()
    data = {
        'id': pet_id,
        'name': request.form['name'],
        'type': request.form['type'],
        'user_id': request.form['user_id']
    }
    Pet.pet_update(data)
    return redirect(f'/pets/{pet_id}')

@app.route('/pets/<int:pet_id>/destroy')
def pet_destroy(pet_id):
    data = {
        'id': pet_id,
    }
    Pet.delete_pet(data)
    return redirect('/pets')
