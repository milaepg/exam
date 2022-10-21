from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
from flask_app.models import user_model 

class Plant:
    db_name = 'arbortrary'
    def __init__(self,data):
        self.id = data['id']
        self.species = data['species']
        self.location = data['location']
        self.reason = data['reason']
        self.date_planted = data['date_planted']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.creator = None
    
    @classmethod
    def create_arbitrarily(cls,data):
        query = "INSERT INTO tree (species, location, reason, date_planted, user_id) VALUES (%(species)s, %(location)s, %(reason)s, %(date_planted)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)
    @classmethod
    def delete_arbitrarily(cls,data):
        query = "DELETE FROM tree WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data) 
    @classmethod
    def update_arbitrarily(cls,data):
        query = "UPDATE tree SET species=%(species)s, location=%(location)s, reason=%(reason)s, date_planted =%(date_planted)s, WHERE tree.id=%(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)    
    
    @classmethod
    def get_tree_by_id(cls, data):
        query = "SELECT * FROM tree WHERE id = %(id)s;"
        return cls(connectToMySQL(cls.db_name).query_db(query, data)[0])

    @staticmethod
    def validate_form(tree):
        is_valid = True 
        if len(tree['species']) < 5:
            flash("The species must be at least 5 characters.", "danger")
            is_valid = False
        if len(tree['location']) < 2:
            flash("The Location must be at least 2 characters.", "danger")
            is_valid = False
        if len(tree['reason']) < 15:
            flash("The Location must be at least 15 characters.", "danger")
            is_valid = False    
        return is_valid 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM tree;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_tree = []
        for row in results:
            all_tree.append( cls(row) )
        return all_tree 