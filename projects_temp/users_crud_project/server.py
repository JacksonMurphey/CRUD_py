from users_crud_app import app
from users_crud_app.controllers import users_controller, pets_controller


if __name__ == '__main__':
    app.run(debug=True)
# this allows the app to run, and debug allows for errors and autoupdating webpages. 