import streamlit as st
from modules.nav import SideBarLinks


# Employer Profile Page
st.set_page_config(layout='wide')
st.title(f"Welcome, {st.session_state.get('name', 'Employer')}!")
SideBarLinks()

st.write("### Your Employer Dashboard")
st.write("""
This is your personalized dashboard where you can:
- Manage job postings.
- Review applications.
- Communicate with candidates.
""")