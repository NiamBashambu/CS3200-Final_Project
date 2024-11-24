

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
        SELECT ResumeId, StudentId, Content, LastUpdated 
        FROM Resume
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
    
# ------------------------------------------------------------
# Updates an existing resume by resumeId
@resume.route('/resume/<int:resumeId>', methods=['PUT'])
def update_resume(resumeId, updatedContent):
    query = '''
        UPDATE Resume
        SET Content = updatedContent
        WHERE ResumeId = {resumeId}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
    