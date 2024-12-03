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
def update_employment(studentId):
    try:
        # Get the new status from the request
        data = request.json
        status = data.get("employmentStatus")

        if not status:
            return jsonify({"error": "Missing 'employmentStatus'"}), 400
        
        # Update the database
        query = '''
            UPDATE StudentSearching
            SET EmployStatus = %s
            WHERE StudentId = %s
        '''
        conn = db.get_db()
        cursor = conn.cursor()
        cursor.execute(query, (status, studentId))
        conn.commit()
        
        return jsonify({"message": "Employment status updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ------------------------------------------------------------
# Gets employment status of a specific student
@studentSearching.route('/studentSearching/<int:studentId>', methods=['GET'])
def get_student_employment(studentId):
    try:
        query = '''
            SELECT EmployStatus
            FROM StudentSearching
            WHERE StudentId = %s
        '''
        cursor = db.get_db().cursor()
        cursor.execute(query, (studentId,))
        theData = cursor.fetchone()

        if not theData:
            return jsonify({"error": "Student not found"}), 404

        return jsonify({"employmentStatus": theData[0]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------------------------------------------------
# Adds a new student record
@studentSearching.route('/studentSearching', methods=['POST'])
def add_student():
    try:
        data = request.json
        student_id = data.get("studentId")
        employment_status = data.get("employmentStatus")

        if not student_id or not employment_status:
            return jsonify({"error": "Missing 'studentId' or 'employmentStatus'"}), 400

        query = '''
            INSERT INTO StudentSearching (StudentId, EmployStatus)
            VALUES (%s, %s)
        '''
        conn = db.get_db()
        cursor = conn.cursor()
        cursor.execute(query, (student_id, employment_status))
        conn.commit()

        return jsonify({"message": "Student added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------------------------------------------------
# Deletes a student record
@studentSearching.route('/studentSearching/<int:studentId>', methods=['DELETE'])
def delete_student(studentId):
    try:
        query = '''
            DELETE FROM StudentSearching
            WHERE StudentId = %s
        '''
        conn = db.get_db()
        cursor = conn.cursor()
        cursor.execute(query, (studentId,))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "Student not found"}), 404

        return jsonify({"message": "Student deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
