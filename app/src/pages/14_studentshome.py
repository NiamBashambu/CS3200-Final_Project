import streamlit as st
from modules.nav import SideBarLinks


# Student Searching Profile Page
st.set_page_config(layout='wide')
st.title(f"Welcome, {st.session_state.get('name', 'Student')}!")
SideBarLinks()
st.write("### Explore COOP Opportunities")
st.write("""
As a student searching for a COOP, you can:
- Browse available COOP opportunities.
- Apply to jobs that match your profile.
- Track your application status.
""")