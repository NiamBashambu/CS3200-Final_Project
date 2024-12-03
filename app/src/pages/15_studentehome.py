import streamlit as st
from modules.nav import SideBarLinks


# Student Exploring Profile Page
st.set_page_config(layout='wide')
st.title(f"Welcome, {st.session_state.get('name', 'Student')}!")
SideBarLinks()
st.write("### Explore Career Paths")
st.write("""
As a student exploring career options, you can:
- Learn about different industries and roles.
- Attend career guidance workshops.
- Save fields of interest.
""")