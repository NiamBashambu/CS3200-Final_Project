from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db



# Create a new Blueprint object for resume
resume = Blueprint('resume', __name__)

# ------------------------------------------------------------
# Get resumes for all existing students
@resume.route('/resume', methods=['GET'])
def get_all_resume():
    query = '''
        SELECT ResumeId, S.Name, S.StudentId, Content, LastUpdated 
        FROM Resume R
        JOIN Student S ON S.StudentId = R.StudentId
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
    
# ------------------------------------------------------------
# Gets resume of specific student
@resume.route('/resume/<int:studentId>', methods=['GET'])
def get_student_resume(studentId):
    query = '''
        SELECT ResumeId, S.Name, S.StudentId, Content, LastUpdated 
        FROM Resume R
        JOIN Student S ON S.StudentId = R.StudentId
        WHERE S.StudentId = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (studentId))
    theData = cursor.fetchone()
    
    if theData:
        response = make_response(jsonify(theData))
        response.status_code = 200
    else:
        response = make_response(jsonify({"error": "No resume found for this student."}))
        response.status_code = 404
    return response


# ------------------------------------------------------------
# Updates an existing resume by resumeId
@resume.route('/resume/<int:resumeId>', methods=['PUT'])
def update_resume(resumeId):
    try:
        updatedContent = request.json.get('Content')
        last_updated = request.json.get('LastUpdated')
        
        query = f'''
            UPDATE Resume
            SET Content = %s, LastUpdated = %s
            WHERE ResumeId = %s
        '''
        cursor = db.get_db().cursor()
        cursor.execute(query, (updatedContent, last_updated, resumeId))
        db.get_db().commit()
        
        return jsonify({"message": "Employment status updated successfully"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    