from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db



# Create a new Blueprint object for resume
student = Blueprint('student', __name__)

# ------------------------------------------------------------
# Gets list of all students
@student.route('/student', methods=['GET'])
def get_all_student():
    query = '''
        SELECT StudentId, Name, Email, Phone, YOG, Major, Advisor
        FROM Student
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
