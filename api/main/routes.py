"""ROutes file containing the url end points"""

from main.models import persona,db
from main.models import persona_schema
from flask import jsonify
from flask import current_app as app

import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property  # To deal with ImportError: cannot import name 'cached_property' from 'werkzeug'  when importing flask restplus
import flask.scaffold       # To deal with ImportError: cannot import name '_endpoint_from_view_func' from 'flask.helpers' when importing flask restplus
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask_restplus import Resource,Api



#Initialising lask Restplus  application with flask app
api = Api(
    app=app, title="CACI API project demo",
    description = "This is an Restful which returns profiles from a "
                  "PostgreSQL database. This API has two GET methods and "
                  "a DELETE method. Hope you enjoy using it !!!",
    contact = "Shafiq Kyazze",
)


Persona_Schema = persona_schema() #To serialize queries
Personas_Scehma = persona_schema(many=True)


"""Get specific profile from database"""
@api.route("/search/<Username>")
class search_for_person(Resource):
    def get(self,Username):
        profile = persona.query.filter(persona.username == Username).first()
        if profile is None:
            return jsonify({"msg": "Information requested is not available in the database"})
        json_profile = Persona_Schema.dump(profile)
        return json_profile


"""Return all existing profiles in the database"""
@api.route("/people")
class return_all_profiles(Resource):
    def get(self):
        profiles = persona.query.limit(1000).all()  #Limiting to the first 1000 due to space reasons
        json_profiles = Personas_Scehma.dump(profiles)
        return json_profiles

"""Delete a profile"""
@api.route("/people/<username>", methods=['DELETE'])
class delete_single_profile(Resource):
    def delete(self,username):
        profile_to_delete = persona.query.filter(persona.username == username).first()
        if profile_to_delete is not None:
            db.session.delete(profile_to_delete)
            db.session.commit()
            return jsonify({"msg": "Profile was deleted from database"})
        return jsonify({"msg": "Information requested is not  available in the database"})