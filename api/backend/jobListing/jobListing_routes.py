
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db



# Create a new Blueprint object for posts
jobListing = Blueprint('joblisting', __name__)

# Get all job listings
@jobListing.route('/jobListing', methods=['GET'])
def get_all_jobListing():
    query = '''
        SELECT jl.CompanyId,  jl.JobId, cj.CompanyName, 
               jl.Department, jl.Description, jl.PostDate, jl.ApplicationLink, jl.Location,jl.Position
        FROM CompanyJobs cj
        JOIN JobListing jl ON cj.CompanyId = jl.CompanyId
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

    

# ------------------------------------------------------------
# Create a new job listing
@jobListing.route('/jobListing', methods=['POST'])
def create_post():
    

    try:
        # Parse the incoming JSON data
        data = request.json
        job_id = data['JobId']
        position = data['Position']
        company_id = data['CompanyId']
        department = data['Department']
        description = data['Description']
        location = data['Location']
        post_date = data['PostDate']
        application_link = data['ApplicationLink']
        

        # Database connection
        db_conn = db.get_db()
        cursor = db_conn.cursor()

        # Check if the company exists
        check_company_query = "SELECT * FROM Company WHERE CompanyId = %s"
        cursor.execute(check_company_query, (company_id,))
        company_exists = cursor.fetchone()

        if not company_exists:
            # Populate the Company table if the company does not exist
            insert_company_query = '''
                INSERT INTO Company (CompanyId) Values(%s)
            '''
            cursor.execute(insert_company_query, (company_id))
            db_conn.commit()

        # Insert the job listing
        insert_job_query = '''
            INSERT INTO JobListing 
            (JobId, Position, CompanyId, Department, Description, Location, PostDate, ApplicationLink)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(insert_job_query, (
            job_id, position, company_id, department, description, location, post_date, application_link
        ))
        db_conn.commit()

        response = make_response("Post created successfully", 201)
        return response

    except KeyError as e:
        # Handle missing keys in the request data
        error_message = f"Missing required field: {str(e)}"
        return jsonify({"error": error_message}), 400

    except Exception as e:
        # Handle unexpected errors
        error_message = f"An error occurred: {str(e)}"
        return jsonify({"error": error_message}), 500

# ------------------------------------------------------------
# Delete a jobListing by JobId
@jobListing.route('/JobListing/<int:JobId>', methods=['DELETE'])
def delete_jobListing(jobId):
    query = f'''
        DELETE FROM JobListing WHERE JobId = {jobId}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Job listing deleted successfully")
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Get job listings with a specific position
@jobListing.route('/jobListing/<position>', methods=['GET'])
def get_jobListing_position(position):
    query = f'''
        SELECT JobId, Position, CompanyId, Department, Description 
        FROM JobListing 
        WHERE Position = {position}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Get the description of a job by jobId
@jobListing.route('/jobListing/<int:jobId>/<description>', methods=['GET'])
def get_job_description(jobId):
    query = f'''
        SELECT Description 
        FROM JobListing 
        WHERE JobId = {jobId}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Gets job listings of a specific location
@jobListing.route('/jobListing/<location>', methods=['GET'])
def get_job_location(location):
    query = f'''
        SELECT JobId, Position, CompanyId, Department, Description, Location
        FROM JobListing
        WHERE Location = {location}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Gets job listings that have been recently posted
@jobListing.route('/jobListing/<postDate>', methods=['GET'])
def get_job_date(location):
    query = f'''
        SELECT JobId, Position, CompanyId, Department, Description, Location
        FROM JobListing
        ORDER BY PostDate
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


