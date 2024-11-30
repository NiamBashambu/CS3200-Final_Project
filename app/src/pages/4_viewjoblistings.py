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

# Custom CSS for global styling
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f4f7fb;
        margin: 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar links (if any)
SideBarLinks()

# Title for Streamlit
st.markdown("<div style='display: flex; justify-content: space-between; align-items: center;'>", unsafe_allow_html=True)
st.title("💼 Job Listings")
st.markdown("</div>", unsafe_allow_html=True)

# Display user's first name if authenticated
if st.session_state.get("authenticated"):
    user_name = st.session_state.get("name", "Guest")
    st.write(f"Hello, {user_name}! 👋 Welcome to the JobListing Feed")

# Fetch Job Listings Automatically from API
try:
    jobs = requests.get(BASE_URL).json()
    jobs = sorted(jobs, key=lambda x: datetime.strptime(x["PostDate"], "%a, %d %b %Y %H:%M:%S %Z"), reverse=True)
except Exception as e:
    st.error(f"Error fetching or parsing job listings: {e}")
    jobs = []

# Display all job listings by default
st.markdown("### All Job Listings")

# Get unique departments for filtering
departments = list(set([job.get("Department") for job in jobs if job.get("Department")]))

# Optional filter
with st.expander("🔍 Filter by Department (Optional)"):
    selected_departments = st.multiselect("Choose Department(s)", departments, default=[])

# Apply filter only if selected
filtered_jobs = [job for job in jobs if job.get("Department") in selected_departments] if selected_departments else jobs

# Display job listings or show appropriate message
if not jobs:  # Case 1: No job listings fetched
    st.markdown(
        """
        <div style='text-align: center; margin: 20px; font-size: 18px; color: #555;'>
            <b>No job listings are currently available. Please check back later.</b>
        </div>
        """,
        unsafe_allow_html=True,
    )
elif not filtered_jobs:  # Case 2: No job listings match the filter
    st.markdown(
        """
        <div style='text-align: center; margin: 20px; font-size: 18px; color: #555;'>
            <b>No job listings match your selected filter criteria.</b>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:  # Case 3: Display job listings
    for job in filtered_jobs:
        job_id = job.get("JobId")
        company_name = job.get("CompanyName")
        position = job.get("Position")
        post_date = job.get("PostDate")
        description = job.get("Description")
        location = job.get("Location")
        application_link = job.get("ApplicationLink")
        department = job.get("Department")

        # Render job post
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
