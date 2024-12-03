import streamlit as st
from modules.nav import SideBarLinks


# Student Searching Profile Page
st.set_page_config(layout='wide')
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
st.title(f"Welcome, {st.session_state.get('name', 'Student')}!")
SideBarLinks()
st.write("### Explore COOP Opportunities")
st.write("""
As a student searching for a COOP, you can:
- Browse available COOP opportunities.
- Create posts to communicate with other students.
- Update your resume. 
""")