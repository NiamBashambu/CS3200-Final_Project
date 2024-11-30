import logging
import streamlit as st
import requests
from datetime import datetime
from modules.nav import SideBarLinks
# Base API URL
BASE_URL = "http://web-api:4000/s/student"
st.set_page_config(layout="wide", page_title="Student Profile", page_icon="👨‍🎓")

# Custom CSS
st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f2f5;
    }
    .post-container {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    .post-header {
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
    }
    .post-content {
        font-size: 14px;
        color: #555;
        margin-bottom: 10px;
    }
    .post-footer {
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
    .action-container {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 20px;
    }
    .add-post-btn, .delete-post-btn {
        background-color: #007bff;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 50%;
        font-size: 18px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .add-post-btn:hover, .delete-post-btn:hover {
        background-color: #0056b3;
    }
    .profile-icon {
        position: absolute;
        top: 10px;
        right: 20px;
        background-color: #007bff;
        color: white;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        text-align: center;
        line-height: 40px;
        cursor: pointer;
        transition: background-color 0.3s;
        font-size: 18px;
    }
    .profile-icon:hover {
        background-color: #0056b3;
    }
    
    """,
    unsafe_allow_html=True,
)

SideBarLinks()
# Page title
st.title("👤 Student Profile")


# Check if the user is authenticated
if "authenticated" in st.session_state and st.session_state["authenticated"]:
    # Get user data from session state
    user_name = st.session_state.get('name', 'Guest')
    student_id = st.session_state.get('student_id', 'Unknown')  # Ensure StudentId is saved in session state

    st.write(f"Hello, {user_name}! 👋 Welcome to your Student Profile page.")

    # Ensure we have a student ID to fetch their profile
    if student_id:
        # Construct the API request URL to fetch only the specific student profile
        student = requests.get(f"{BASE_URL}/{student_id}").json()

        if student:
            
            st.success("Student details retrieved successfully!")
            st.write("### Student Information")
            st.write(f"**Student ID:** {student.get('StudentId','N/A')}")
            st.write(f"**Name:** {user_name}")
            st.write(f"**Email:** {student.get('Email', 'N/A')}")
            st.write(f"**Phone:** {student.get('Phone', 'N/A')}")
            st.write(f"**Year of Graduation:** {student.get('YOG', 'N/A')}")
            st.write(f"**Major:** {student.get('Major', 'N/A')}")
            st.write(f"**Advisor:** {student.get('COA.Name', 'N/A')}")
            st.write(f"**Employed Status:** {student.get('SS.EmployStatus', 'N/A')}")
            
        else:
            st.error(f"Error fetching student details: ")
    else:
        st.error("Student ID is missing from session state.")
else:
    st.write("You are not authenticated. Please log in to view your profile.")