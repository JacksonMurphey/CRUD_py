from users_crud_app import app
## here we are importing the app created in __init__.py
from flask import render_template, redirect, request
## since we imported the app from __init__.py, when we say from flask, we dont need to import Flask as it was already imported on the __init__.py file. we can just import what routing types we will use.
from users_crud_app.models.user import User
## here we are importing the class instance of User to create routes for user class. 
from users_crud_app.models.pet import Pet



@app.route('/users')
def user_dashboard():
    users = User.get_all()
    # users = User.get_user_pet()
    return render_template('users_dash.html', users=users)

@app.route('/users/new')
def user_new():
    return render_template('users_new.html')

@app.route('/users/create', methods=['POST'])
def user_create():
    User.save(request.form)
    return redirect('/users')

@app.route('/users/<int:user_id>')
def display_user(user_id):
    user = User.show_user(user_id)
    # user = User.get_user_pet(user_id)
    return render_template('show_user.html', user=user)

@app.route('/users/<int:user_id>/edit')
def edit_user_page(user_id):
    user = User.show_user(user_id)
    # data = {'id': user_id} 
    #user = User.show_user(data)
    return render_template('user_edit.html', user=user)


@app.route('/users/<int:user_id>/update', methods = ['POST'])
def update_user(user_id):
    data = {
        'id': user_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    User.user_update(data)
    return redirect(f'/users/{user_id}')

@app.route('/users/<int:user_id>/destroy')
def user_destroy(user_id):
    data = {
        'id': user_id,
    }
    user.delete(data)
    return redirect('/users')