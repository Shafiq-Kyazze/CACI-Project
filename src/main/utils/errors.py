from flask import jsonify,make_response
from flask import current_app as app
from utils.responses  import *

@app.errorhandler(404)
def person_not_in_db(err):
    response = jsonify(error=str(err)), 404
    return response