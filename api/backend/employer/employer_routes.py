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
SELECT e.EmployerId, e.Name, e.Email, e.Phone, e.CompanyId, CompanyName
        FROM Employer e
        LEFT JOIN Company c ON e.CompanyId = c.CompanyId
        LEFT JOIN CompanyJobs ON e.CompanyId = CompanyJobs.CompanyId
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

# ------------------------------------------------------------
# Add a new employer
@employer.route('/employer', methods=['POST'])
def add_employer():
    try:
        data = request.json
        name = data.get("Name")
        email = data.get("Email")
        phone = data.get("Phone")
        company_id = data.get("CompanyId")

        if not name or not email or not phone or not company_id:
            return jsonify({"error": "Missing required fields: 'Name', 'Email', 'Phone', or 'CompanyId'"}), 400

        query = '''
            INSERT INTO Employer (Name, Email, Phone, CompanyId)
            VALUES (%s, %s, %s, %s)
        '''
        conn = db.get_db()
        cursor = conn.cursor()
        cursor.execute(query, (name, email, phone, company_id))
        conn.commit()

        return jsonify({"message": "Employer added successfully"}), 201
    except Exception as e:
        current_app.logger.error(f"Error adding employer: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

# ------------------------------------------------------------
# Update employer information
@employer.route('/employer/<int:employerId>', methods=['PUT'])
def update_employer(employerId):
    try:
        data = request.json
        name = data.get("Name")
        email = data.get("Email")
        phone = data.get("Phone")
        company_id = data.get("CompanyId")

        if not any([name, email, phone, company_id]):
            return jsonify({"error": "At least one field (Name, Email, Phone, CompanyId) must be provided for update"}), 400

        updates = []
        values = []

        if name:
            updates.append("Name = %s")
            values.append(name)
        if email:
            updates.append("Email = %s")
            values.append(email)
        if phone:
            updates.append("Phone = %s")
            values.append(phone)
        if company_id:
            updates.append("CompanyId = %s")
            values.append(company_id)

        query = f'''
            UPDATE Employer
            SET {", ".join(updates)}
            WHERE EmployerId = %s
        '''
        values.append(employerId)

        conn = db.get_db()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"message": "Employer not found"}), 404

        return jsonify({"message": "Employer updated successfully"}), 200
    except Exception as e:
        current_app.logger.error(f"Error updating employer: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

# ------------------------------------------------------------
# Delete an employer
@employer.route('/employer/<int:employerId>', methods=['DELETE'])
def delete_employer(employerId):
    try:
        query = '''
            DELETE FROM Employer
            WHERE EmployerId = %s
        '''
        conn = db.get_db()
        cursor = conn.cursor()
        cursor.execute(query, (employerId,))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"message": "Employer not found"}), 404

        return jsonify({"message": "Employer deleted successfully"}), 200
    except Exception as e:
        current_app.logger.error(f"Error deleting employer: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500
