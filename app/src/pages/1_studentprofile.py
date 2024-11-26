import logging
import streamlit as st
import requests
from datetime import datetime
from modules.nav import SideBarLinks


# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


BASE_URL = "http://web-api:4000/s/student"

# Set page layout to wide
st.set_page_config(layout="wide", page_title="Student Profie", page_icon="👨‍🎓")

# Custom CSS
st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f2f5;
    }
    .student-container {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    .student-header {
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
    }
    .student-content {
        font-size: 14px;
        color: #555;
        margin-bottom: 10px;
    }
    .student-footer {
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
# Title for the Streamlit app
st.title("Student Profile")
st.write("")

# Display Section Title for Students
st.write("Student Profile")

# Fetch Students Automatically from the API
students = requests.get(BASE_URL)


if students:
    for student in students:
        student_id = student.get("StudentId")
        student_name = student.get("Name")
        student_email = student.get("Email")
        student_YOG = student.get("YOG")
        student_major = student.get("Major")
        
        with st.container():
                st.markdown('<div class="student-container">', unsafe_allow_html=True)
                # Post Header: Student Info and Post Category
                st.markdown(
                    f"""
                    <div class="student-header">
                        <span>🎓 <b>Student {student_name}</b></span>
                        <span style="float:right; color:#888;">{student_major}</span>
                        <span style="float:right; color:#888;">{student_YOG}</span>
                        <span style="float:right; color:#888;">{student_email}</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                

            
       
else:
    st.write("No students found.")
