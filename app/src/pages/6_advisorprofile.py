import logging
import streamlit as st
import requests
from datetime import datetime
from modules.nav import SideBarLinks

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Base API URL for CoOpAdvisor
BASE_URL = "http://web-api:4000/a/advisor"  # Adjust the endpoint to match your backend setup

# Set page layout to wide
st.set_page_config(layout="wide", page_title="CoOp Advisor Profile", page_icon="👩‍🏫")

# Custom CSS
st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f2f5;
    }
    .advisor-container {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    .advisor-header {
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
    }
    .advisor-content {
        font-size: 14px;
        color: #555;
        margin-bottom: 10px;
    }
    .advisor-footer {
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
st.title("👩‍🏫 CoOp Advisor Profile")

# Check if the user is authenticated
if "authenticated" in st.session_state and st.session_state["authenticated"]:
    # Get user data from session state
    user_name = st.session_state.get('name', 'Guest')
    advisor_id = st.session_state.get('advisor_id', 'Unknown')  # Ensure AdvisorId is saved in session state

    st.write(f"Hello, {user_name}! 👋 Welcome to your CoOp Advisor Profile page.")

    # Ensure we have an advisor ID to fetch their profile
    if advisor_id:
        # Construct the API request URL to fetch only the specific advisor profile
        advisor = requests.get(f"{BASE_URL}/{advisor_id}").json()

        if advisor:
            st.success("CoOp Advisor details retrieved successfully!")
            st.write("### Advisor Information")
            st.write(f"**Advisor ID:** {advisor.get('CoopAdvisorID', 'N/A')}")
            st.write(f"**Name:** {advisor.get('Name', 'N/A')}")
            st.write(f"**Department:** {advisor.get('Department', 'N/A')}")
            st.write(f"**Field of Study:** {advisor.get('Field', 'N/A')}")
        else:
            st.error(f"Error fetching CoOp Advisor details.")
    else:
        st.error("Advisor ID is missing from session state.")
else:
    st.write("You are not authenticated. Please log in to view your profile.")
