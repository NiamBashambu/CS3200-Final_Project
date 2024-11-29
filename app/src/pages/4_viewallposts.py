import logging
import streamlit as st
import requests
from datetime import datetime
from modules.nav import SideBarLinks

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

BASE_URL = "http://web-api:4000/p/posts"

# Set page layout to wide
st.set_page_config(layout="wide", page_title="Post Feed", page_icon="💬")

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
st.title("💬 Post Feed")
st.markdown("</div>", unsafe_allow_html=True)

# Display the user's first name if authenticated
if st.session_state.get("authenticated"):
    user_name = st.session_state.get('name', 'Guest')
    st.write(f"Hello, {user_name}! 👋 Welcome to the Post Feed")

# Fetch Posts Automatically from the API
posts = requests.get(BASE_URL).json()
try:
    posts = sorted(posts, key=lambda x: datetime.strptime(x["PostDate"], "%a, %d %b %Y %H:%M:%S %Z"), reverse=True)
except ValueError as e:
    st.error(f"Error parsing date: {e}")

# Display posts if available
if posts:
    for post in posts:
        post_id = post.get("PostId")
        student_name = post.get("Name")
        content = post.get("Content")
        post_date = post.get("PostDate")
        category = post.get("Category")
            
        # Wrap everything inside the post container
        with st.container():
            
            # Post Header: Student Info and Post Category
            st.markdown(
                f"""
                <div class="post-header">
                    <span>🎓 <b>{student_name}</b></span>
                    <span>{category}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )
            
            # Post Date
            st.markdown(
                f"<div style='color: #888; font-size: 14px;'>📅 {post_date}</div>",
                unsafe_allow_html=True,
            )
            
            # Post Content
            st.markdown(
                f"<div class='post-content'>{content}</div>",
                unsafe_allow_html=True,
            )
else:
    st.write("No posts found.")
