import logging
import streamlit as st
import requests
from datetime import datetime
from modules.nav import SideBarLinks

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

BASE_URL = "http://web-api:4000/r/resume"

# Set page layout to wide
st.set_page_config(layout="wide", page_title="Upload/Update Resume", page_icon="📝")

# Custom CSS for fancy styling
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f4f7fb;
        margin: 0;
    }
    .post-container {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease-in-out;
    }
    .post-container:hover {
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        transform: translateY(-5px);
    }
    .post-header {
        font-weight: 600;
        font-size: 18px;
        color: #333;
        margin-bottom: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .post-header span {
        font-size: 14px;
        color: #888;
    }
    .post-content {
        font-size: 16px;
        color: #555;
        line-height: 1.8;
        margin-bottom: 20px;
    }
    .post-footer {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 10px;
    }
    .action-button {
        background-color: #007bff;
        color: white;
        padding: 8px 15px;
        border-radius: 20px;
        font-size: 14px;
        cursor: pointer;
        border: none;
        transition: background-color 0.3s ease;
    }
    .action-button:hover {
        background-color: #0056b3;
    }
    .add-post-btn {
        background-color: #28a745;
        color: white;
        font-size: 28px;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        display: flex;
        justify-content: center;
        align-items: center;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .add-post-btn:hover {
        background-color: #218838;
    }
    .form-container {
        background-color: #ffffff;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        margin-top: 50px;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    .form-container input, .form-container textarea {
        width: 100%;
        padding: 12px;
        margin-bottom: 20px;
        border-radius: 10px;
        border: 1px solid #ddd;
        font-size: 16px;
        transition: border-color 0.3s ease;
    }
    .form-container input:focus, .form-container textarea:focus {
        border-color: #007bff;
        outline: none;
    }
    .form-container .submit-btn {
        background-color: #007bff;
        color: white;
        padding: 12px 20px;
        border-radius: 30px;
        font-size: 18px;
        cursor: pointer;
        border: none;
        width: 100%;
    }
    .form-container .submit-btn:hover {
        background-color: #0056b3;
    }
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }
    .header-container h1 {
        font-size: 32px;
        color: #333;
    }
    .profile-icon {
        background-color: #007bff;
        color: white;
        font-size: 24px;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .profile-icon:hover {
        background-color: #0056b3;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar links (if any)
SideBarLinks()

# Title for the Streamlit app
st.markdown("<div class='header-container'>", unsafe_allow_html=True)
st.title("📝 Upload Resume")
st.markdown("</div>", unsafe_allow_html=True)

# Display the user's first name if authenticated
if st.session_state.get("authenticated"):
    user_name = st.session_state.get('name', 'Guest')
    student_id = st.session_state.get('student_id', 'Unknown')

    st.write(f"Hello, {user_name}! 👋 Upload or update your resume here.")

# Check if student already has an existing resume
try:
    resume = requests.get(f'{BASE_URL}/{student_id}').json()
    if resume and resume.get('Content'):
        st.write('Current Resume:')
    else:
        # no resume associated with student
        st.write('No existing resume found. Upload one here!')
        resume = None

except ValueError as e:
    st.error(f"Error fetching resume: {e}")


# Display resume if it already exists
if resume is not None:
    name = resume.get("Name")
    student_id = resume.get("StudentId")
    resume_id = resume.get('ResumeId')
    content = resume.get("Content")
    lastupdated = datetime.strptime(resume.get("LastUpdated"), "%a, %d %b %Y %H:%M:%S %Z").date()
    
    st.markdown(
            f"""
            <div style="background-color: #ffffff; border-radius: 15px; padding: 25px; margin-bottom: 30px;
                        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);">
                <div style="font-weight: 600; font-size: 18px; color: #333; margin-bottom: 10px;
                            display: flex; justify-content: space-between; align-items: center;">
                    <span><b>Name: {name}</b> | <b>Student ID: {student_id}</b></span>
                </div>
                <div style="font-size: 16px; color: #555; line-height: 1.8; margin-bottom: 20px;">
                    {content}
                </div>
                <div style="display: flex; justify-content: flex-end; align-items: center; gap: 10px;">
                    Updated on {lastupdated}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# Add a button to upload/update resume
with st.container():
    if "show_form" not in st.session_state:
        st.session_state["show_form"] = False

    def toggle_form():
        st.session_state["show_form"] = not st.session_state["show_form"]

    # Plus button to toggle form visibility
    st.button("➕ Upload/Update Resume", key="toggle_form", on_click=toggle_form, use_container_width=True)

# Display the resume creation form if the state is toggled
if st.session_state["show_form"]:
    st.write("### ✍️ Upload/Update your resume")
    with st.form(key="upload_resume", clear_on_submit=True):
        # Automatically pre-fill the Student Name and ID field with the logged-in info
        student_id = st.session_state.get('student_id', 'Unknown')
        content = st.text_area("Content", placeholder="Resume goes here")
        lastupdated = st.date_input("Last Updated", value=datetime.now().date())
        lastupdated = lastupdated.strftime('%Y-%m-%d')
    
        submit = st.form_submit_button(label="Upload/Update Resume", use_container_width=True)
        
        if submit:
            upload_resume = {
                "Content": content,
                'LastUpdated': lastupdated
            }

            if resume != None:
                try:
                    response = requests.put(f'{BASE_URL}/{resume_id}', json = upload_resume)
                    if response.status_code == 200:
                        st.success("Resume updated successfully!")

                        # Refetch the updated resume data
                        resume = requests.get(f'{BASE_URL}/{student_id}').json()

                        name = resume.get("Name")
                        student_id = student_id
                        resume_id = resume_id
                        content = content
                        lastupdated = lastupdated
    
                        st.markdown(
                            f"""
                            <div style="background-color: #ffffff; border-radius: 15px; padding: 25px; margin-bottom: 30px;
                                        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);">
                                <div style="font-weight: 600; font-size: 18px; color: #333; margin-bottom: 10px;
                                            display: flex; justify-content: space-between; align-items: center;">
                                    <span><b>Name: {name}</b> | <b>Student ID: {student_id}</b></span>
                                </div>
                                <div style="font-size: 16px; color: #555; line-height: 1.8; margin-bottom: 20px;">
                                    {content}
                                </div>
                                <div style="display: flex; justify-content: flex-end; align-items: center; gap: 10px;">
                                    Updated on {lastupdated}
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
                    else:
                        st.error(f"Failed to update resume: {response.text}")
                except Exception as e:
                    st.error(f"Error updating resume: {e}")

            else:
                try:
                    response = requests.post(f'{BASE_URL}/{student_id}', json = upload_resume)
                    if response.status_code == 200:
                        st.success("Resume uploaded successfully!")

                        # Refetch the updated resume data
                        resume = requests.get(f'{BASE_URL}/{student_id}').json()

                        name = resume.get("Name")
                        student_id = student_id
                        content = content
                        lastupdated = lastupdated
    
                        st.markdown(
                            f"""
                            <div style="background-color: #ffffff; border-radius: 15px; padding: 25px; margin-bottom: 30px;
                                        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);">
                                <div style="font-weight: 600; font-size: 18px; color: #333; margin-bottom: 10px;
                                            display: flex; justify-content: space-between; align-items: center;">
                                    <span><b>Name: {name}</b> | <b>Student ID: {student_id}</b></span>
                                </div>
                                <div style="font-size: 16px; color: #555; line-height: 1.8; margin-bottom: 20px;">
                                    {content}
                                </div>
                                <div style="display: flex; justify-content: flex-end; align-items: center; gap: 10px;">
                                    Updated on {lastupdated}
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
                    else:
                        st.error(f"Failed to upload resume: {response.text}")
                except Exception as e:
                    st.error(f"Error upload resume: {e}")


            




