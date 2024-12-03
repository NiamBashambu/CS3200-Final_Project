
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
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 201
    return response

# ------------------------------------------------------------
# Get all notifications
@notification.route('/notification', methods=['GET'])
def get_all_notifications():
    try:
        query = '''
            SELECT * 
            FROM Notification
        '''
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()

        if not theData:
            return jsonify({"message": "No notifications found"}), 404

        return jsonify(theData), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------------------------------------------------
# Get a specific notification by ID
@notification.route('/notification/<int:notif_id>', methods=['GET'])
def get_notification(notif_id):
    try:
        query = '''
            SELECT * 
            FROM Notification
            WHERE NotifId = %s
        '''
        cursor = db.get_db().cursor()
        cursor.execute(query, (notif_id,))
        theData = cursor.fetchone()

        if not theData:
            return jsonify({"message": "Notification not found"}), 404

        return jsonify(theData), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------------------------------------------------
# Update a notification
@notification.route('/notification/<int:notif_id>', methods=['PUT'])
def update_notification(notif_id):
    try:
        data = request.json
        content = data.get('Content')
        timestamp = data.get('TimeStamp')

        if not content and not timestamp:
            return jsonify({"error": "Nothing to update"}), 400

        updates = []
        values = []

        if content:
            updates.append("Content = %s")
            values.append(content)

        if timestamp:
            updates.append("TimeStamp = %s")
            values.append(timestamp)

        query = f'''
            UPDATE Notification
            SET {", ".join(updates)}
            WHERE NotifId = %s
        '''
        values.append(notif_id)

        conn = db.get_db()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"message": "Notification not found"}), 404

        return jsonify({"message": "Notification updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------------------------------------------------
# Delete a notification
@notification.route('/notification/<int:notif_id>', methods=['DELETE'])
def delete_notification(notif_id):
    try:
        query = '''
            DELETE FROM Notification
            WHERE NotifId = %s
        '''
        conn = db.get_db()
        cursor = conn.cursor()
        cursor.execute(query, (notif_id,))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"message": "Notification not found"}), 404

        return jsonify({"message": "Notification deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
