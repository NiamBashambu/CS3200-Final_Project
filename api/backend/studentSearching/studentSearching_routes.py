from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db



# Create a new Blueprint object for resume
studentSearching = Blueprint('studentSearching', __name__)

# ------------------------------------------------------------
# Gets employment status of every student
@studentSearching.route('/studentSearching/<employmentStatus>', methods=['GET'])
def get_all_student():
    query = '''
        SELECT EmployStatus
        FROM StudentSearching
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response