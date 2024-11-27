
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db



# Create a new Blueprint object for posts
posts = Blueprint('posts', __name__)

# ------------------------------------------------------------
# Get all posts
@posts.route('/posts', methods=['GET'])
def get_all_posts():
    query = '''
        SELECT PostId, s.StudentId, Content, PostDate, Category, s.Name 
        FROM Posts JOIN Student s
        ON s.StudentID = Posts.StudentId
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
    

# ------------------------------------------------------------
# Create a new post
@posts.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    student_id = data['StudentId']
    content = data['Content']
    post_date = data['PostDate']
    category = data['Category']
    
    query = f'''
        INSERT INTO Posts (StudentId, Content, PostDate, Category)
        VALUES ({student_id}, '{content}', '{post_date}', '{category}')
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Post created successfully")
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


