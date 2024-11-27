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
    current_app.logger.info(f'GET /student Result of query = {theData}')


    
    response = make_response(jsonify(theData))
    

    response.status_code = 200
    return response

# ------------------------------------------------------------
# Returns all information of a particular student
@student.route('/student/<int:studentId>', methods=['GET'])
def get_student_information(studentId):
    query = f'''
        SELECT StudentId, Name, Email, Phone, YOG, Major, Advisor
        FROM Student
        WHERE StudentId = {studentId}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Gets the major of a particular student
@student.route('/student/<int:studentId>/<major>', methods=['GET'])
def get_student_major(studentId):
    query = f'''
        SELECT Major
        FROM Student 
        WHERE StudentId = {studentId}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response