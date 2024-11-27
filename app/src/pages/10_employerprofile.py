import logging
import streamlit as st
import requests
import db
from datetime import datetime
from modules.nav import SideBarLinks


# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

BASE_URL = "http://web-api:4000/employer"

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

def fetch_profile(id):
    query = 'SELECT * FROM employers WHERE EmployerId = :EmployerId'
    profile = db.fetch_one(query, {'EmployerId': id})
    return profile

st.title('Employer Profile')

st.write('')

if st.session_state.get("authenticated"):
    id = st.session_state.get('id', '1')

    if id is not None:
        profile = fetch_profile(id)
        st.write(f"Hello, {profile['Name']}! 👋 What would you like to do today?")