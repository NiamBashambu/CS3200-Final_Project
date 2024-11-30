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