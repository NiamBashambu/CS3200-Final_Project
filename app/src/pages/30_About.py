import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About this App")

st.markdown (
    """
    This is CO-Connect. 
    A Facebook like app for CO-OPs. 

    Stay tuned for more information and features to come!
    """
        )
