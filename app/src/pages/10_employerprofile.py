import logging
import streamlit as st
import requests
from datetime import datetime
from modules.nav import SideBarLinks

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Base API URL for Employer
BASE_URL = "http://web-api:4000/e/employer"

# Set page layout to wide
st.set_page_config(layout="wide", page_title="Employer Profile", page_icon="🧑‍💼")

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
st.title("👤 Employer Profile")

# Check if the user is authenticated
if "authenticated" in st.session_state and st.session_state["authenticated"]:
    # Get user data from session state
    user_name = st.session_state.get('name', 'Guest')
    employer_id = st.session_state.get('employer_id', 'Unknown')  # Ensure EmployerId is saved in session state

    st.write(f"Hello, {user_name}! 👋 Welcome to your Employer Profile page.")

    # Ensure we have an employer ID to fetch their profile
    if employer_id:
        # Construct the API request URL to fetch only the specific employer profile
        employer = requests.get(f"{BASE_URL}/{employer_id}").json()

        if employer:
            st.success("Employer details retrieved successfully!")
            st.write("### Employer Information")
            st.write(f"**Employer ID:** {employer.get('EmployerId', 'N/A')}")
            st.write(f"**Company ID:** {employer.get('CompanyId','N/A')}")
            company_name = employer.get('CompanyName', 'N/A')

            st.write(f"**Company Name:** {company_name}")
  
            st.write(f"**Contact Email:** {employer.get('Email', 'N/A')}")
            st.write(f"**Contact Phone:** {employer.get('Phone', 'N/A')}")
        else:
            st.error(f"Error fetching employer details: ")
    else:
        st.error("Employer ID is missing from session state.")
else:
    st.write("You are not authenticated. Please log in to view your profile.")