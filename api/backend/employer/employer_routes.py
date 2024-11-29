from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db



# Create a new Blueprint object for posts
employer = Blueprint('employer', __name__)

# ------------------------------------------------------------
# Get all employers
@employer.route('/employer', methods=['GET'])
def get_all_employers():
    query = '''
        SELECT EmployerId, Name, Email, Phone, CompanyId 
        FROM Employer
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


@employer.route('/employer/<int:employerId>', methods=['GET'])
def get_employer_information(employerId):
    query = '''
        SELECT e.EmployerId, e.Name, e.Email, e.Phone, e.CompanyId, cj.CompanyName
        FROM Employer e
        JOIN Company c ON e.CompanyId = c.CompanyId
        JOIN CompanyJobs cj ON e.CompanyId = cj.CompanyId
        WHERE e.EmployerId = %s
    '''
    
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (employerId,))
        theData = cursor.fetchone()

        if theData is None:
            current_app.logger.error(f'Employer with ID {employerId} not found.')
            return jsonify({'error': 'Employer not found'}), 404

        # Return the data wrapped in a response
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response

    except Exception as e:
        current_app.logger.error(f"Error fetching employer information: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

