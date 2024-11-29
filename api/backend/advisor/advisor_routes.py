from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

# Create a new Blueprint object for advisors
advisors = Blueprint('advisors', __name__)

# ------------------------------------------------------------
# Get all advisors
@advisors.route('/advisor', methods=['GET'])
def get_all_advisors():
    query = '''
        SELECT CoopAdvisorID, Name, Department, Field
        FROM CoOpAdvisor
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Get information about a specific advisor by CoopAdvisorID
@advisors.route('/advisor/<int:advisorId>', methods=['GET'])
def get_advisor_information(advisorId):
    query = '''
        SELECT CoopAdvisorID, Name, Department, Field
        FROM CoOpAdvisor
        WHERE CoopAdvisorID = %s
    '''
    
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (advisorId,))
        theData = cursor.fetchone()
        
        if theData is None:
            current_app.logger.error(f'Advisor with ID {advisorId} not found.')
            return jsonify({'error': 'Advisor not found'}), 404

        # Return the data wrapped in a response
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response

    except Exception as e:
        current_app.logger.error(f"Database error: {e}")
        return jsonify({'error': 'Internal server error'}), 500