"""Global errors"""

from flask import jsonify,make_response
from flask import current_app as app
#from utils.responses  import *

@app.errorhandler(400)
def person_not_in_db(err):
    #Person types in wrong url handle
    response = jsonify({'msg':"Check the API documentation for more information on this API's endpoint and how to use the API please"})
    return response, 400

@app.errorhandler(500)
def api_fault(err):
    response = jsonify({'msg': "Sorry our service is experiencing a few issues. But our team are right on it"})
    return response , 500

@app.errorhandler(404)
def person_not_in_db(err):
    #Person types in wrong url handle
    response = jsonify({'msg':"Check the you URL and the method used. For more information, check the API's documentation"})
    return response, 404

@app.errorhandler(405)
def person_not_in_db(err):
    #Person types in wrong url handle
    response = jsonify({'msg':"Check the your URL and method and make sure they correspond. For more information, check the API's documentation"})
    return response, 405