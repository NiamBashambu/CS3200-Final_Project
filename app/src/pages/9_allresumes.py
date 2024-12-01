import logging
import streamlit as st
import requests
from datetime import datetime
from modules.nav import SideBarLinks

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Base API URL for job listings
BASE_URL = "http://web-api:4000/r/resume"

# Page configuration
st.set_page_config(layout="wide", page_title="Student Resumes", page_icon="📝")

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
st.title("📝 Student Resumes")
st.markdown("</div>", unsafe_allow_html=True)

# Display user's first name if authenticated
if st.session_state.get("authenticated"):
    user_name = st.session_state.get("name", "Guest")
    st.write(f"Hello, {user_name}! 👋 View All Student Resumes Here")


# Fetch Resumes Automatically from API
try:
    resumes = requests.get(BASE_URL)
    resumes.raise_for_status()
    resumes = resumes.json()
    resumes = sorted(resumes, key=lambda x: datetime.strptime(x["LastUpdated"], "%a, %d %b %Y %H:%M:%S %Z").date())


except Exception as e:
    st.error(f"Error fetching or parsing resumes: {e}")
    resumes = []

# Search by name
search = st.text_input('Search for resume by student name')

# initialize filtered resumes, returns all resumes if no search
filtered_resumes = resumes

if search:
    search = search.lower()
    filtered_resumes = [resume for resume in resumes if search in resume.get("Name", "").lower()]


# Display all job listings by default
st.markdown("### Resumes")

# Display job listings or show appropriate message
if not resumes:  # Case 1: No resumes fetched
    st.markdown(
        """
        <div style='text-align: center; margin: 20px; font-size: 18px; color: #555;'>
            <b>No resumes were found. Please check back later.</b>
        </div>
        """,
        unsafe_allow_html=True,
    )
elif not filtered_resumes:  # Case 2: No resume found for student
    st.markdown(
        """
        <div style='text-align: center; margin: 20px; font-size: 18px; color: #555;'>
            <b>No resumes match your selected filter criteria.</b>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:  # Case 3: Display resume listings
    for resume in filtered_resumes:
        name = resume.get("Name")
        student_id = resume.get("StudentId")
        content = resume.get("Content")
        lastupdated = resume.get("LastUpdated")

        # Render resume entry
        st.markdown(
            f"""
            <div style="background-color: #ffffff; border-radius: 15px; padding: 25px; margin-bottom: 30px;
                        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);">
                <div style="font-weight: 600; font-size: 18px; color: #333; margin-bottom: 10px;
                            display: flex; justify-content: space-between; align-items: center;">
                    <span><b>Name: {name}</b> | <b>Student ID: {student_id}</b></span>
                </div>
                <div style="font-size: 16px; color: #555; line-height: 1.8; margin-bottom: 20px;">
                    {content}
                </div>
                <div style="display: flex; justify-content: flex-end; align-items: center; gap: 10px;">
                    Updated on {lastupdated}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
