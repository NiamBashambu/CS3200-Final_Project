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


@student.route('/student/check_or_create', methods=['POST'])
def check_or_create_student():
    data = request.json
    student_id = data.get("StudentId")
    name = data.get("Name")

    # Check if the student exists
    query_check = f'''
        SELECT StudentId, Name, Email, Phone, YOG, Major, Advisor
        FROM Student
        WHERE StudentId = {student_id}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query_check)
    student = cursor.fetchone()

    if student:
        current_app.logger.info(f"Student found: {student}")
        response = make_response(jsonify(student))
        response.status_code = 200
        return response

    # If the student doesn't exist, create a new entry
    query_insert = f'''
        INSERT INTO Student (StudentId, Name)
        VALUES ({student_id}, "{name}")
    '''
    try:
        cursor.execute(query_insert)
        db.get_db().commit()
        current_app.logger.info(f"Student created: {student_id}, {name}")
        response = make_response(jsonify({"message": "Student created", "StudentId": student_id, "Name": name}))
        response.status_code = 201
        return response
    except Exception as e:
        current_app.logger.error(f"Error creating student: {e}")
        response = make_response(jsonify({"error": str(e)}))
        response.status_code = 400
        return response