import logging
import streamlit as st
import requests
import pandas as pd
from datetime import datetime
from modules.nav import SideBarLinks

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

BASE_URL = "http://web-api:4000/s/student"

# Set page layout to wide
st.set_page_config(layout="wide", page_title="Student Profile", page_icon="👨‍🎓")

# Custom CSS for styling
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
    .student-table th {
        text-align: left;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar links
SideBarLinks()

# Title for the Streamlit app
st.title("All Student Profiles")

# Fetch Students Automatically from the API
students = requests.get(BASE_URL).json()
if "authenticated" in st.session_state and st.session_state["authenticated"]:
    # Get user data from session state
    user_name = st.session_state.get('name', 'Guest')
    advisor_id = st.session_state.get('advisor_id', 'Unknown')  # Ensure StudentId is saved in session state

    st.write(f"Hello, {user_name}! 👋 Welcome to your managing Student Profiles page.")

    if students:
        # get a list of all majors
        majors = list(set(student.get("Major") for student in students))
        statuses = ['Employed', 'Searching', 'Not Searching']

        with st.expander('Filter students by major and status'):
            filter_major = st.multiselect("Filter by Major", majors, default=[])
            filter_status = st.multiselect("Filter by Employment Status", statuses, default=[])
    
        
        # initialize filtering, return all students if no filtering
        filtered_students = students
        
        if filter_major:
            filtered_students = [student for student in filtered_students if student.get("Major") in filter_major]

        if filter_status:
            filtered_students = [student for student in filtered_students if student.get("EmployStatus") in filter_status]  

        


        # Create a list to hold student data for the DataFrame
        student_data = []

        for student in filtered_students:
            student_id = student.get("StudentId")
            student_name = student.get("Name")
            student_email = student.get("Email")
            student_YOG = student.get("YOG")
            student_major = student.get("Major")
            student_status = student.get('EmployStatus')
        
        # Add each student's data to the list
            student_data.append([student_id, student_name, student_email, student_YOG, student_major, student_status])

    # Convert the list of student data into a pandas DataFrame
        df = pd.DataFrame(student_data, columns=["Student ID", "Name", "Email", "Year of Graduation (YOG)", "Major", 'Employment Status'])
        df.index = df.index + 1

    # Display the students data in a table format
        st.markdown(
        """
        <div class="student-container">
            <div class="student-header">
                <b>All Students Information</b>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Display the dataframe as a table in Streamlit
        st.dataframe(df)
    else:
        st.write("No students found.")
else:
    st.write("You are not authenticated. Please log in to view your profile.")


