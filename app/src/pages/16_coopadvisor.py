import streamlit as st
from modules.nav import SideBarLinks


# COOP Advisor Profile Page
st.set_page_config(layout='wide')
st.title(f"Welcome, {st.session_state.get('name', 'Advisor')}!")
SideBarLinks()
st.write("### Advisor Dashboard")
st.write("""
As a COOP advisor, you can:
- Guide students in their COOP search.
- Approve job postings.
- Monitor COOP program success.
""")