from users_crud_app.config.mysqlconnection import connectToMySQL
## vvv this is importing the pet.py file, not the class Pet
from users_crud_app.models import pet 

class User:
    ##attributes
    def __init__(self, data):##constructor - expected to be a dictionary
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.pets = [] ## NOTE this will be a list of pet objects that we will create by appending below.

    ##methods
    @classmethod
    def get_all(cls):
        ## query 
        query = 'SELECT * FROM users;'
        ## actually query the DB
        results = connectToMySQL('users_schema').query_db(query)
        ## new list to append objects to
        users = []
        ## for loop
        for user in results: 
        ## turn dicts into objects
            users.append(cls(user))
        ## return new list of object 
        return users

    @classmethod
    def save(cls, data): ## used to create a user, we will need data, to get data we need a form, pass that to the controller, then save the data and pass it to the DB
        query = 'INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW() );'
        return connectToMySQL('users_schema').query_db(query, data)


    # @classmethod 
    # def get_user_pet(cls, data):
    #     query = 'SELECT * FROM users LEFT JOIN pets on pets.user_id = users.id WHERE users.id = %(id)s;' 
    #     results = connectToMySQL('users_schema').query_db(query,data)
    #     user = cls(results[0])

    #     for pet_dict in results:
    #         pet_data = {
    #             'id': pet_dict['pet.id'],
    #             'name': pet_dict['name'],
    #             'type': pet_dict['type'],
    #             'created_at': pet_dict['pet.created_at'],
    #             'updated_at': pet_dict['pet.updated_at']
    #         }
    #         user.pets.append(pet.Pet(pet_data))
    #     return user


    @classmethod
    def show_user(cls, user_id):
        ##getting one user .. platform refers to this method as get_one()
        query = 'SELECT * FROM users WHERE users.id = %(id)s;' 
        data = {'id': user_id }
        results = connectToMySQL('users_schema').query_db(query, data)
        user = cls(results[0])
        return user

    ## not sure yet how to set this up. pass user/data to my function?
    @classmethod
    def user_update(cls, data):
        
        query = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE users.id = %(id)s;'
        
        return connectToMySQL('users_schema').query_db(query, data)


    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM users WHERE users.id = %(id)s;'
        return connectToMySQL('users_scema').query_db(query, data)



    # ## NOTE: this is how we will assoicate Pets with Users 
    # @classmethod 
    # def get_user_with_pet(cls, data):
    #     query = 'SELECT * FROM users LEFT JOIN pets ON pets.user_id = users.id WHERE users.id = %(id)s;'
        
    #     results = connectToMySQL('users_schema').query_db(query, data)
        
    #     user = cls(results[0])
    #     for row_from_db in results:
    #         ## Now we will parse the pet data to make instances of pets and add them into out list above.
    #         pet_data = {
    #             'id' : row_from_db['pets.id'],
    #             'name' : row_from_db['name'],
    #             'type' : row_from_db['type'],
    #             'created_at' : row_from_db['pets.created_at'],
    #             'updated_at' : row_from_db['pets.updated_at']
    #         }
    #         user.pets.append( pet.Pet(pet_data))
    #     return user