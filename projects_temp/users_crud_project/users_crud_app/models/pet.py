from users_crud_app.config.mysqlconnection import connectToMySQL
## copied code form user.py and updated where necessary
## use command-F to find all instances of the word User, then you can replace it with Pet.
from users_crud_app.models import user

class Pet:
    ##attributes
    def __init__(self, data):##constructor - expected to be a dictionary
        ## do not need to put forgein keys here. 
        self.id = data['id']
        self.name = data['name']
        self.type = data['type']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
        self.user_id = data['user_id']

    ##methods
    @classmethod
    def get_all(cls):
        ## query 
        query = 'SELECT * FROM pets;'
        ## actually query the DB
        results = connectToMySQL('users_schema').query_db(query)
        ## new list to append objects to
        pets = []
        ## for loop
        for pet in results: 
        ## turn dicts into objects
            pets.append(cls(pet))
        ## return new list of object 
        return pets


    @classmethod
    def save(cls, data): ## used to create a user, we will need data, to get data we need a form, pass that to the controller, then save the data and pass it to the DB

        ##NOTE here we need to put the forgein key.
        query = 'INSERT INTO pets (name, type, user_id, created_at, updated_at) VALUES (%(name)s, %(type)s, %(user_id)s, NOW(), NOW() );'
        return connectToMySQL('users_schema').query_db(query, data)


    @classmethod
    def show_pet(cls, pet_id):
        
        query = 'SELECT * FROM pets JOIN users on users.id = pets.user_id WHERE pets.id = %(id)s;' 
        data = {'id': pet_id }
        
        results = connectToMySQL('users_schema').query_db(query, data)
        pet = cls(results[0])
        user_data = { 
            'id' : results[0]['users.id'],
            'first_name' : results[0]['first_name'],
            'last_name' : results[0]['last_name'],
            'email' : results[0]['email'],
            'created_at' : results[0]['users.created_at'],
            'updated_at' : results[0]['users.updated_at']
        }
        pet.user = user.User(user_data)
        return pet

## this method currently isnt working. 
    # @classmethod
    # def pet_update(cls, data):
    #     query = "UPDATE pets SET name = %(name)s, type = %(type)s, user_id = %(user_id)s, update_at = NOW() WHERE pets.id = %(id)s;"
        
    #     return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def delete_pet(csl, data):
        query = 'DELETE FROM pets WHERE pets.id = %(id)s'
        return connectToMySQL('users_schema').query_db(query, data)



## not sure if this is how to do this. 
    # @classmethod
    # def pet_update(cls, pet_id):
    #     query = "UPDATE pets SET name = %(name)s, type = %(type)s, user_id = %(user_id)s, update_at = NOW() WHERE pets.id = %(id)s;"
    #     data = {'id': pet_id}
    #     results = connectToMySQL('users_schema').query_db(query, data)
    #     pet = cls(results[0])
    #     user_data = { 
    #         'id' : results[0]['users.id'],
    #         'first_name' : results[0]['first_name'],
    #         'last_name' : results[0]['last_name'],
    #         'email' : results[0]['email'],
    #         'created_at' : results[0]['users.created_at'],
    #         'updated_at' : results[0]['users.updated_at']
    #     }
    #     pet.user_id = user.User(user_data)
       
    #     return pet





#NOTE for many to many relationships by double joining, this allows us to display multiple pieces of data, rewatch 9/30 lecture. we basically copy user_data{from above} and copy same for another instance of a class. 
    # @classmethod
    # def get_one_complete(cls, data):
    #     query = 'SELECT * FROM pets JOIN users on users.id = pets.user_id WHERE pets.id = %(id)s;' 

## NOTE: ok so this what I copied from my user.py, this allows the pet data to be displayed. However, since im not JOINing the user table, its not pulling their USER_id #, thus its not displaying any value in that position 
    # @classmethod
    # def show_pet(cls, pet_id):
        
    #     query = 'SELECT * FROM pets WHERE id = %(id)s;' 
    #     data = {'id': pet_id }
    #     results = connectToMySQL('users_schema').query_db(query, data)
    #     pet = cls(results[0])
    #     return pet

    # @classmethod 
    # def get_pet_with_user(cls, data):
    #     query = 'SELECT * FROM pets JOIN users ON users.id = pets.user_id WHERE pets.id = %(id)s;'
        
    #     results = connectToMySQL('users_schema').query_db(query, data)
        
    #     pet = cls(results[0])
    #     for row_from_db in results:
    #         ## Now we will parse the pet data to make instances of pets and add them into out list above.
    #         user_data = {
    #             'id' : row_from_db['users.id'],
    #             'first_name' : row_from_db['first_name'],
    #             'last_name' : row_from_db['last_name'],
    #             'email' : row_from_db['email'],
    #             'created_at' : row_from_db['users.created_at'],
    #             'updated_at' : row_from_db['users.updated_at']
    #         }
    #         pet.users.append( user.User(user_data))
    #     return pet