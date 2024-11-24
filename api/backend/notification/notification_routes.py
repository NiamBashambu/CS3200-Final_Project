
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db



# Create a new Blueprint object for posts
notification = Blueprint('notification', __name__)

# ------------------------------------------------------------
# Create a new notification
@notification.route('/notification', methods=['POST'])
def create_notification():
    data = request.json
    notif_id = data['NotifId']
    post_id = data['PostId']
    job_id = data['JobId']
    student_id = data['StudentId']
    timestamp = data['TimeStamp']
    content = data['Content']
    
    query = f'''
        INSERT INTO Notification (NotifId, PostId, JobId, StudentId, TimeStamp, Content)
        VALUES ({notif_id}, {post_id}, {job_id}, {student_id}, {timestamp}, {content})
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Notification created successfully")
    response.status_code = 201
    return response
