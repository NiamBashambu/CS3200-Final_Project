########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################

from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db



# Create a new Blueprint object for posts
posts = Blueprint('employer', __name__)

# ------------------------------------------------------------
# Get all employers
@posts.route('/employer', methods=['GET'])
def get_all_employers():
    query = '''
        SELECT EmployerId, Name, Email, Phone, CompanyId 
        FROM Employer
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
