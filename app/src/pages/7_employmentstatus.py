import logging
import streamlit as st
import requests
from datetime import datetime
from modules.nav import SideBarLinks

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

BASE_URL = "http://web-api:4000/t/studentSearching/"

# Set page layout to wide
st.set_page_config(layout="wide", page_title="Post Feed", page_icon="💬")

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

# Title for the Streamlit app
st.markdown("<div class='header-container'>", unsafe_allow_html=True)
st.title("💼 Update Employment Status")
st.markdown("</div>", unsafe_allow_html=True)

# Display the user's first name if authenticated
if st.session_state.get("authenticated"):
    user_name = st.session_state.get('name', 'Guest')
    student_id = st.session_state.get('student_id', 'Unknown')  # Ensure StudentId is saved in session state

    st.markdown(f"Hello, {user_name} 👋")

# Employment status options
    employment_status_options = ['Employed', 'Searching', 'Not Searching']
    
    # Form for employment status update
    with st.form(key="employment_status_form"):
        # Select the current employment status
        current_status = st.selectbox("Select Your Current Employment Status", employment_status_options)
        
        # Submit button
        submit_button = st.form_submit_button("Update Status")
        
        # If the form is submitted
        if submit_button:
            # Make an API request to update the employment status
            response = requests.put(f"{BASE_URL}/{student_id}", json={"employmentStatus": current_status})

            if response.status_code == 200:
                st.success("Your employment status has been updated successfully!")
            else:
                st.error(f"Error: {response.status_code} - {response.text or 'Unknown error'}")

else:
    st.error("You need to be logged in to update your employment status.")