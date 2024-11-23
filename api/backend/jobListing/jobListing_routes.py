########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################

from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db



# Create a new Blueprint object for posts
posts = Blueprint('jobListing', __name__)

# ------------------------------------------------------------
# Get all job listings
@posts.route('/jobListing', methods=['GET'])
def get_all_jobListing():
    query = '''
        SELECT JobId, Position, CompanyId, Department, Description 
        FROM JobListing
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
    

# ------------------------------------------------------------
# Create a new job listing
@posts.route('/jobListing', methods=['POST'])
def create_post():
    data = request.json
    job_id = data['JobId']
    position = data['Position']
    company_id = data['CompanyId']
    department = data['Department']
    description = data['Description']
    
    query = f'''
        INSERT INTO JobListing (JobId, Position, CompanyId, Department, Description)
        VALUES ({job_id}, '{position}', '{company_id}', '{department}', '{description})
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Job listing created successfully")
    response.status_code = 201
    return response

# ------------------------------------------------------------
# Delete a post by PostId
@posts.route('/posts/<int:postId>', methods=['DELETE'])
def delete_post(postId):
    query = f'''
        DELETE FROM Posts WHERE PostId = {postId}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Post deleted successfully")
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Get the content of a specific post
@posts.route('/posts/<int:postId>/<content>', methods=['GET'])
def get_post_content(postId, content):
    query = f'''
        SELECT Content FROM Posts WHERE PostId = {postId}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchone()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Get the email of the student who made a post
@posts.route('/posts/<int:studentId>/<email>', methods=['GET'])
def get_student_email(studentId, email):
    query = f'''
        SELECT Email FROM Student WHERE StudentId = {studentId}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchone()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Get the date a specific post was made
@posts.route('/posts/<int:postId>/<PostDate>', methods=['GET'])
def get_post_date(postId, PostDate):
    query = f'''
        SELECT PostDate FROM Posts WHERE PostId = {postId}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchone()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


