"""routes.py"""
from main.models import persona,persona_schema,db,USERS,users_schema
from flask import jsonify,request
from flask import current_app as app
from flask_login import current_user,login_user
from flask_jwt_extended import create_access_token,jwt_required
from datetime import timedelta

persona_Schema = persona_schema()
personas_Scehma = persona_schema(many=True)
USER_SCHEMA = users_schema()

@app.route("/create",methods=['POST'])
def create_user():
    data = request.get_json()
    if "username" not in data or "password" not in data or "email" not in data:
        return jsonify({"msg":"Please fill in all the fields"})
    if USERS.query.filter_by(login_username=data['username']).first() is not None:
        return jsonify({"msg":'please use a different username'})
    if USERS.query.filter_by(email=data['email']).first() is not None:
        return jsonify({"msg":'please use a different email address'})

    user_details ={}
    user_details['login_username'] = data["username"]
    non_hashed_password = data["password"]
    user_details['email'] = data["email"]
    user_details['login_password'] = USERS.generate_hash_password(non_hashed_password)

    new_user = USER_SCHEMA.load(user_details)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg":"Your registration was successful"})


@app.route("/login",methods=['POST'])
def login():
    username = request.json["username"]
    password = request.json["password"]
    auth_data = USERS.query.filter(USERS.login_username == username).first()
    if auth_data is None:
        return jsonify({"msg":"Username doesn't exist. Please enter valid credentials or sign up"})
    if USERS.check_password(auth_data.login_password,password):
        access_token = create_access_token(identity=username, expires_delta=timedelta(minutes=30))
        return jsonify({"msg":"Login was successful", "Username":username, "Access Token": access_token})
    return jsonify({"msg":"Invalid password. Please enter valid information or sign up"})


#Get specific profile from database
@app.route("/search/<Username>", methods=['GET'])
@jwt_required
def search_for_person(Username):
    profile = persona.query.filter(persona.username == Username).first()
    print(profile)
    if profile is None:
        return jsonify({"msg": "Information requested is not available in the database"})
    json_profile = persona_Schema.jsonify(profile)
    return json_profile


#Return all existing profiles in the database
@app.route("/people",methods=['GET'])
@jwt_required
def return_all_profiles():
    profiles = persona.query.all()
    json_profiles = jsonify(personas_Scehma.dump(profiles))
    return json_profiles

#Delete a profile
@app.route("/delete/people/<username>", methods=['DELETE'])
@jwt_required
def delete_profile(username):
    profile_to_delete = persona.query.filter(persona.username == username).first()
    if profile_to_delete is not None:
        db.session.delete(profile_to_delete)
        db.commit()
        return jsonify({"msg": "Profile was deleted from database"})
    return jsonify({"msg": "Information requested is not  available in the database"})