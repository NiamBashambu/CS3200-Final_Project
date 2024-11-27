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

# Custom CSS
st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f2f5;
    }
    .post-container {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    .post-header {
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
    }
    .post-content {
        font-size: 14px;
        color: #555;
        margin-bottom: 10px;
    }
    .post-footer {
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
    .action-container {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 20px;
    }
    .add-post-btn, .delete-post-btn {
        background-color: #007bff;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 50%;
        font-size: 18px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .add-post-btn:hover, .delete-post-btn:hover {
        background-color: #0056b3;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

SideBarLinks()

# Title for the Streamlit app
st.title("💬 Posts")
st.write("")
# Display the user's first name if authenticated
if st.session_state.get("authenticated"):
    user_name = st.session_state.get('name', 'Guest')
    st.write(f"Hello, {user_name}! 👋 Welcome to the Post Feed")
# Display Section Title for Posts
st.write("### 📰 Posts Feed")

# Fetch Posts Automatically from the API
posts = requests.get(BASE_URL).json()
try:
    posts = sorted(posts, key=lambda x: datetime.strptime(x["PostDate"], "%a, %d %b %Y %H:%M:%S %Z"), reverse=True)
except ValueError as e:
    st.error(f"Error parsing date: {e}")

# Add a button to add a post
with st.container():
    st.markdown(
        """
        <div class="action-container">
            <button class="add-post-btn" onclick="window.location.reload();">➕</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

if posts:
    for post in posts:
        post_id = post.get("PostId")
        student_id = post.get("StudentId")
        content = post.get("Content")
        post_date = post.get("PostDate")
        category = post.get("Category")
        student_name = post.get("Name")
            
        with st.container():
            st.markdown('<div class="post-container">', unsafe_allow_html=True)
            # Post Header: Student Info and Post Category
            st.markdown(
                f"""
                <div class="post-header">
                    <span>🎓 <b>Student {student_name}</b></span>
                    <span style="float:right; color:#888;">{category}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )
            # Post Date
            st.markdown(
                f"<div style='color: #888; font-size: 12px;'>📅 {post_date}</div>",
                unsafe_allow_html=True,
            )
            # Post Content
            st.markdown(
                f"<div class='post-content'>{content}</div>",
                unsafe_allow_html=True,
            )
            
            
            # Button for deleting the post
            if st.button(f"Delete Post {post_id}", key=f"delete_{post_id}"):
                response = requests.delete(f"{BASE_URL}/{post_id}")
                if response.status_code == 200:
                    st.success(f"Post {post_id} has been deleted successfully!")
                else:
                    st.error("Failed to delete the post. Please try again.")
            
            st.markdown("</div>", unsafe_allow_html=True)
else:
    st.write("No posts found.")


# Spacing between sections
st.write("")
st.write("")
st.write("### 📝 Create or Manage Posts")



    # Display the post creation form when the button is clicked
st.write("### ✍️ Create a New Post")
with st.form(key="create_post"):
        # Automatically pre-fill the Student Name field with the logged-in user's name
        student_name = st.session_state.get('name', 'Guest')
        student_id = st.text_input("Student ID", placeholder="Enter your Student ID")
        content = st.text_area("Content", placeholder="What's on your mind?")
        post_date = st.date_input("Post Date", value=datetime.now().date())
        category = st.text_input("Category", placeholder="Enter a category (e.g., News, Updates)")
        
        # Automatically fill the student's name in the form
        st.text_input("Student Name", value=student_name, disabled=True)  # Name field is pre-filled and disabled

        
        submit_button = st.form_submit_button(label="Post")
        if submit_button:
            post_data = {
                "StudentId": student_id,
                "Content": content,
                "PostDate": str(post_date),
                "Category": category,
                "Name": student_name  # Pass the logged-in user's name with the post
            }
            response = requests.post(BASE_URL, json=post_data)
            if response.status_code == 201:
                st.success("Your post has been created successfully!")
            else:
                st.error("Failed to create the post. Please try again.")
