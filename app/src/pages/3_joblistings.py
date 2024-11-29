import logging
import streamlit as st
import requests
from datetime import datetime
from modules.nav import SideBarLinks

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Base API URL for job listings
BASE_URL = "http://web-api:4000/j/jobListings"

# Page configuration
st.set_page_config(layout="wide", page_title="Job Listings", page_icon="💼")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .job-container {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .job-container:hover {
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    .job-header {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .job-details {
        font-size: 14px;
        color: #555;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.title("💼 Job Listings")

# Sidebar
st.sidebar.header("Navigation")
st.sidebar.write("Select a page:")
st.sidebar.button("Job Listings")

# Section: Add a New Job Listing
st.subheader("Create a New Job Listing")
with st.form(key="job_form"):
    company_name = st.text_input("Company Name", placeholder="Enter the company's name")
    position = st.text_input("Position", placeholder="Enter the job title/position")
    department = st.text_input("Department", placeholder="Enter the department name")
    job_description = st.text_area("Job Description", placeholder="Provide a detailed job description")
    location = st.text_input("Location", placeholder="Enter the job location")
    application_link = st.text_input("Application Link", placeholder="Provide a link for applications")
    submit = st.form_submit_button("Post Job")

    # If form is submitted
    if submit:
        if not company_name or not position or not department or not job_description or not location or not application_link:
            st.error("Please fill in all required fields.")
        else:
            # Payload for the API
            payload = {
                "CompanyName": company_name,
                "Position": position,
                "Department": department,
                "Description": job_description,
                "Location": location,
                "PostDate": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "ApplicationLink": application_link,
            }

            try:
                # API Call to create a new job listing
                response = requests.post(BASE_URL, json=payload)
                if response.status_code == 201:
                    st.success("Job listing created successfully!")
                else:
                    st.error(f"Failed to create job listing: {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Section: View All Job Listings
st.subheader("Available Job Listings")

try:
    # Fetch all job listings from the API
    job_listings = requests.get(BASE_URL).json()

    if job_listings:
        for job in job_listings:
            company_name = job.get("CompanyName")
            position = job.get("Position")
            department = job.get("Department")
            description = job.get("Description")
            location = job.get("Location")
            post_date = job.get("PostDate")
            application_link = job.get("ApplicationLink")

            # Job Listing Card
            with st.container():
                st.markdown(
                    f"""
                    <div class="job-container">
                        <div class="job-header">{position}</div>
                        <div class="job-details">Company: {company_name}</div>
                        <div class="job-details">Department: {department}</div>
                        <div class="job-details">Location: {location}</div>
                        <div class="job-details">Posted on: {post_date}</div>
                        <div>{description}</div>
                        <div><a href="{application_link}" target="_blank">Apply Here</a></div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
    else:
        st.write("No job listings available at the moment.")
except Exception as e:
    st.error(f"Failed to fetch job listings: {e}")
