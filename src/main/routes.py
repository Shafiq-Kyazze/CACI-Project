"""routes.py"""
from main.models import persona,persona_schema,db
from flask import jsonify,request
from flask import current_app as app


persona_Schema = persona_schema()
personas_Scehma = persona_schema(many=True)


#Get specific profile from database
@app.route("/search/<Username>", methods=['GET'])
def search_for_person(Username):
    profile = persona.query.filter(persona.username == Username).first()
    print(profile)
    if profile is None:
        return jsonify({"msg": "Information requested is not available in the database"})
    json_profile = persona_Schema.jsonify(profile)
    return json_profile


#Return all existing profiles in the database
@app.route("/people",methods=['GET'])
def return_all_profiles():
    profiles = persona.query.all()
    json_profiles = jsonify(personas_Scehma.dump(profiles))
    return json_profiles

#Delete a profile
@app.route("/delete/people/<username>", methods=['DELETE'])
def delete_profile(username):
    profile_to_delete = persona.query.filter(persona.username == username).first()
    if profile_to_delete is not None:
        db.session.delete(profile_to_delete)
        db.commit()
        return jsonify({"msg": "Profile was deleted from database"})
    return jsonify({"msg": "Information requested is not  available in the database"})