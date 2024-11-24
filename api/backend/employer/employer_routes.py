from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db



# Create a new Blueprint object for posts
employer = Blueprint('employer', __name__)

# ------------------------------------------------------------
# Get all employers
@employer.route('/employer', methods=['GET'])
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
