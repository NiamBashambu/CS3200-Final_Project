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
def get_all_student_employment():
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

# ------------------------------------------------------------
# Updates the employment status of a student
@studentSearching.route('/studentSearching/<int:studentId>', methods=['PUT'])
def update_employment(studentId, status):
    query = f'''
        UPDATE StudentSearching
        SET EmployStatus = {status}
        WHERE StudentId = {studentId}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (studentId, status))
    cursor.commit()
    
    response = make_response("Employment status updated successfully")
    response.status_code = 200
    return response