import logging
import streamlit as st
import requests
from datetime import datetime
from modules.nav import SideBarLinks
import time

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Base API URL for Employer
EMP_BASE_URL = "http://web-api:4000/e/employer"

# Base API URL for Job Listings
JL_BASE_URL = "http://web-api:4000/j/jobListing"

# Set page layout to wide
st.set_page_config(layout="wide", page_title="Update Job Listings", page_icon="👔")

# Custom CSS
st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f2f5;
    }
    .employer-container {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    .employer-header {
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
    }
    .employer-content {
        font-size: 14px;
        color: #555;
        margin-bottom: 10px;
    }
    .employer-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 15px;
    }
    .action-button {
        border: none;
        color: #555;
        background-color: transparent;
        cursor: pointer;
        font-size: 14px;
        padding: 5px 10px;
    }
    .action-button:hover {
        color: #007bff;
    }
    .action-input {
        width: 100%;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

SideBarLinks()

# Page title
st.title("👔 Update Job Listings")

# Check if the user is authenticated
if "authenticated" in st.session_state and st.session_state["authenticated"]:
    # Get user data from session state
    user_name = st.session_state.get('name', 'Guest')
    employer_id = st.session_state.get('employer_id', 'Unknown')  # Ensure EmployerId is saved in session state
    employee = requests.get(f"{EMP_BASE_URL}/{employer_id}").json()
    
    company_id = employee.get('CompanyId', 'N/A')

    st.write(f"Hello, {user_name}! 👋 Welcome to your Company's Posted Job Listings")

    # Ensure we have an employer ID to fetch their profile
    if company_id:
        try:
            jobs = requests.get(JL_BASE_URL).json()
            jobs = sorted(jobs, key=lambda x: datetime.strptime(x["PostDate"], "%a, %d %b %Y %H:%M:%S %Z"), reverse=True)
        except Exception as e:
            st.error(f"Error fetching or parsing job listings: {e}")
            jobs = []

        filtered_jobs =  [job for job in jobs if job.get("CompanyId") == company_id]


        for job in filtered_jobs:
            job_id = job.get("JobId")
            company_name = job.get("CompanyName")
            position = job.get("Position")
            post_date = job.get("PostDate")
            description = job.get("Description")
            location = job.get("Location")
            application_link = job.get("ApplicationLink")
            department = job.get("Department")

            # Adding the job listings as well as a delete button under each one
            with st.container():

                st.markdown(
                f"""
                <div style="background-color: #ffffff; border-radius: 15px; padding: 25px; margin-bottom: 30px;
                            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);">
                    <div style="font-weight: 600; font-size: 18px; color: #333; margin-bottom: 10px;
                                display: flex; justify-content: space-between; align-items: center;">
                        <span><b>Position: {position}</b> | <b>Company: {company_name}</b></span>
                        <span><b>Location: </b>{location}</span>
                    </div>
                    <div style="font-size: 16px; color: #555; line-height: 1.8; margin-bottom: 20px;">
                        {description}
                    </div>
                    <div style="display: flex; justify-content: flex-end; align-items: center; gap: 10px;">
                        Posted on {post_date} | <a href="{application_link}" target="_blank">Apply Here</a>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
                )

                # Attempts to delete the job listing above
                if st.button("Delete"):
                    try:
                        st.write(f"Attempting to delete job with ID: {job_id}")
                        st.write(f"Attempting to delete with company: {company_name}")
                        st.write(f'{JL_BASE_URL}/{job_id}')
                        response = requests.delete(f'{JL_BASE_URL}/{job_id}')
           
                        if response.status_code == 200:
                            st.write('Job posting successfully deleted.')


                        else:
                            st.error(f"Failed to delete job posting: {response.status_code}, {response.text}")

                    except Exception as e:
                            st.error(f"Error deleting request: {e}")
                
                
                

            

