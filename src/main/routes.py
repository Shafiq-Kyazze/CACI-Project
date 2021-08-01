"""routes.py"""
from main.models import persona,persona_schema,db
from flask import jsonify
from flask import current_app as app
from flask_restplus import Resource,Api


api = Api(
    app=app, title="CACI API project demo",
    description = "This is an Restful which returns profiles from a PostgreSQL database. This API has two GET methods and a DELETE method. Hope you enjoy using it !!!",
    contact = "ShafiqKyazze",
)


persona_Schema = persona_schema()
personas_Scehma = persona_schema(many=True)



#Get specific profile from database
@api.route("/search/<Username>")
class search_for_person(Resource):
    def get(self,Username):
        profile = persona.query.filter(persona.username == Username).first()
        print(profile)
        if profile is None:
            return jsonify({"msg": "Information requested is not available in the database"})
        json_profile = persona_Schema.jsonify(profile)
        return json_profile


#Return all existing profiles in the database
@api.route("/people")
class return_all_profiles(Resource):
    def get(self):
        profiles = persona.query.all()
        json_profiles = jsonify(personas_Scehma.dump(profiles))
        return json_profiles

#Delete a profile
@api.route("/people/<username>", methods=['DELETE'])
class delete_single_profile(Resource):
    def delete(self,username):
        profile_to_delete = persona.query.filter(persona.username == username).first()
        if profile_to_delete is not None:
            db.session.delete(profile_to_delete)
            db.commit()
            return jsonify({"msg": "Profile was deleted from database"})
        return jsonify({"msg": "Information requested is not  available in the database"})