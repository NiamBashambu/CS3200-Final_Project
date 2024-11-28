##################################################
# This the home page for CoConnect
##################################################


import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# import the main streamlit library as well
# as SideBarLinks function from src/modules folder
import streamlit as st
from modules.nav import SideBarLinks

# streamlit supports reguarl and wide layout (how the controls
# are organized/displayed on the screen).
st.set_page_config(layout = 'wide')

# If a user is at this page, we assume they are not 
# authenticated.  So we change the 'authenticated' value
# in the streamlit session_state to false. 
st.session_state['authenticated'] = False

# Use the SideBarLinks function from src/modules/nav.py to control
# the links displayed on the left-side panel. 
# IMPORTANT: ensure src/.streamlit/config.toml sets
# showSidebarNavigation = false in the [client] section
SideBarLinks(show_home=True)

# ***************************************************
#    The major content of this page
# ***************************************************

# set the title of the page and provide a simple prompt. 
logger.info("Loading the Home page of the app")
st.title('Co-Connect')
st.write('\n\n')
st.write('### HI! As which user would you like to log in?')

# For each of the user personas for which we are implementing
# functionality, we put a button on the screen that the user 
# can click to MIMIC logging in as that mock user. 

if st.button("Act as John Doe, an Employer for a company", 
            type = 'primary', 
            use_container_width=True):
    # when user clicks the button, they are now considered authenticated
    st.session_state['authenticated'] = True
    # we set the role of the current user
    st.session_state['role'] = 'employer'
    # we add the first name of the user (so it can be displayed on 
    # subsequent pages). 
    st.session_state['name'] = 'John Doe'
    st.session_state['employer_id'] = 51
    # finally, we ask streamlit to switch to another page, in this case, the 
    # landing page for this particular user type
    st.switch_page('pages/10_employerprofile.py')

if st.button('Act as Olivia Garcia, a student searching for a COOP', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'student_searching'
    st.session_state['name'] = 'Olivia Garcia'
    st.session_state['student_id'] = 51
    st.switch_page('pages/0_post.py')

if st.button('Act as Will Jones, a student exploring different fields', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'student_exploring'
    st.session_state['name'] = 'Will Jones'
    st.session_state['student_id'] = 52
    st.switch_page('pages/2_studentprofile.py')

if st.button('Act as Mary Smith, a COOP advisor ',type = 'primary',use_container_width=True):
        st.session_state['authenticated'] = True
        st.session_state['role']  = 'advisor'
        st.session_state['first_name'] = 'Mary'
        st.switch_page('pages/1_allstudentsprofile.py')



