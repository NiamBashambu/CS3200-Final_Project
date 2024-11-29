import logging
import streamlit as st
import requests
from datetime import datetime
from modules.nav import SideBarLinks

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Base API URL for job listings
BASE_URL = "http://web-api:4000/j/jobListing"

# Page configuration
st.set_page_config(layout="wide", page_title="Job Listings", page_icon="💼")

# Custom CSS for fancy styling
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f4f7fb;
        margin: 0;
    }
    .post-container {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease-in-out;
    }
    .post-container:hover {
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        transform: translateY(-5px);
    }
    .post-header {
        font-weight: 600;
        font-size: 18px;
        color: #333;
        margin-bottom: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .post-header span {
        font-size: 14px;
        color: #888;
    }
    .post-content {
        font-size: 16px;
        color: #555;
        line-height: 1.8;
        margin-bottom: 20px;
    }
    .post-footer {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 10px;
    }
    .action-button {
        background-color: #007bff;
        color: white;
        padding: 8px 15px;
        border-radius: 20px;
        font-size: 14px;
        cursor: pointer;
        border: none;
        transition: background-color 0.3s ease;
    }
    .action-button:hover {
        background-color: #0056b3;
    }
    .add-post-btn {
        background-color: #28a745;
        color: white;
        font-size: 28px;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        display: flex;
        justify-content: center;
        align-items: center;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .add-post-btn:hover {
        background-color: #218838;
    }
    .form-container {
        background-color: #ffffff;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        margin-top: 50px;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    .form-container input, .form-container textarea {
        width: 100%;
        padding: 12px;
        margin-bottom: 20px;
        border-radius: 10px;
        border: 1px solid #ddd;
        font-size: 16px;
        transition: border-color 0.3s ease;
    }
    .form-container input:focus, .form-container textarea:focus {
        border-color: #007bff;
        outline: none;
    }
    .form-container .submit-btn {
        background-color: #007bff;
        color: white;
        padding: 12px 20px;
        border-radius: 30px;
        font-size: 18px;
        cursor: pointer;
        border: none;
        width: 100%;
    }
    .form-container .submit-btn:hover {
        background-color: #0056b3;
    }
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }
    .header-container h1 {
        font-size: 32px;
        color: #333;
    }
    .profile-icon {
        background-color: #007bff;
        color: white;
        font-size: 24px;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .profile-icon:hover {
        background-color: #0056b3;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar links (if any)
SideBarLinks()

# Title for Streamlit
st.markdown("<div class='header-container'>", unsafe_allow_html=True)
st.title("💼 Job Listings")
st.markdown("</div>", unsafe_allow_html=True)

# Display users first name if authenticated
if st.session_state.get("authenticated"):
    user_name = st.session_state.get('name', 'Guest')
    st.write(f"Hello, {user_name}! 👋 Welcome to the JobListing Feed")

# Fetch Job Listings Automatically from API
jobs = requests.get(BASE_URL).json()
try:
    jobs = sorted(jobs, key=lambda x: datetime.strptime(x["PostDate"], "%a, %d %b %Y %H:%M:%S %Z"), reverse=True)
except ValueError as e:
    st.error(f"Error parsing date: {e}")

# Add a button to add a new job
if "show_job_form" not in st.session_state:
    st.session_state["show_job_form"] = False

def toggle_job_form():
    st.session_state["show_job_form"] = not st.session_state["show_job_form"]

st.button("➕ Add Job Listing", on_click=toggle_job_form)

# Display the job creation form
if st.session_state["show_job_form"]:
    st.write("### 📝 Create a New Job Listing")
    with st.form(key="create_job", clear_on_submit=True):
        company_id = st.text_input("Company Id", placeholder="Enter the company Id")
        job_id = st.text_input("Job ID",placeholder="Enter the job id")
        position = st.text_input("Position", placeholder="Enter the job tipositiontle")
        department = st.text_input("Department", placeholder = "Enter the department")
        description = st.text_area("Job Description", placeholder="Enter a detailed job description")
        location = st.text_input("Location", placeholder="Enter the job location")
        posted_date = st.date_input("Posted Date", value=datetime.now().date())
        application_link = st.text_input("Application Link", placeholder="Provide a URL for applications")
        

        submit_button = st.form_submit_button("Submit")
        if submit_button:
            job_data = {
                "JobId":job_id,
                "CompanyId": company_id,
                "Position": position,
                "Description": description,
                "Location": location,
                "PostDate": str(posted_date),
                "ApplicationLink": application_link,
                "Department":department
            }
            try:
                response = requests.post(BASE_URL, json=job_data)
                if response.status_code == 201:
                    st.success("Job listing created successfully!")
                    st.session_state["show_job_form"] = False  # Hide form
                else:
                    st.error(f"Failed to create job listing: {response.text}")
            except Exception as e:
                st.error(f"Error creating job listing: {e}")

# Display job listings
if jobs:
    for job in jobs:
        job_id = job.get("JobId")
        company_name = job.get("CompanyName")
        position = job.get("Position")
        company_id = job.get("CompanyId")
        post_date = job.get("PostDate")
        description = job.get("Description")
        location = job.get("Location")
        application_link = job.get("ApplicationLink")
        department = job.get("Department")
        with st.container():
            st.markdown(
                f"""
                <div class="post-container">
                    <div class="post-header">
                        <span><b>Postion: {position}</b> | <b>Company: {company_name}</b></span>
                        <span><b>Location:</b> {location}</span>
                    </div>
                    <div class="post-content">
                        {description}
                    </div>
                    <div class="post-footer">
                        Posted on {post_date} 
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
else:
    st.write("No job listings available.")