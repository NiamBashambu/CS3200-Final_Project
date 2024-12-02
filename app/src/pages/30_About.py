import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.title('**Co-Connect**')
st.write('Your go-to platform for Co-op opportunities!')

st.subheader("About Us")

st.markdown (
    """
    We are *Co-Connect*, a Facebook like app for Co-ops. <br>

    Our platform addresses the difficulties and frustrations felt by students 
    and employers in the co-op process. Co-ops offer students valuable 
    opportunities to jumpstart their careers in their chosen fields. However, 
    due to the limited information provided in job descriptions, students often
    find themselves realizing too late--once they're already on the job--that 
    the role doesn't meet their needs or expectations. <br>

    NUWorks, the current platform, lacks features such as workload variability, 
    work environment, realistic responsibilities, and much more. Northeastern 
    students need a platform that offers a realistic insight into the co-op world 
    and the industries they are preparing to enter. *Co-Connect* offers a more 
    intuitive, data-driven platform that is tailored to co-ops offered to Northeastern
    students. <br>

    Check out some of our features below!
    """,
        unsafe_allow_html=True)
