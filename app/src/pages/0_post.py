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
    </style>
    """,
    unsafe_allow_html=True,
)
SideBarLinks()
# Title for the Streamlit app
st.title("💬 Post Feed")
st.write("")

# Display Section Title for Posts
st.write("### 📰 Posts Feed")

# Fetch Posts Automatically from the API
posts = requests.get(BASE_URL).json()


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
                # Post Footer: Actions
                st.markdown(
                    """
                    <div class="post-footer">
                        <button class="action-button">👍 Like</button>
                        <button class="action-button">💬 Comment</button>
                        <button class="action-button">🔗 Share</button>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                # Comment input box (conditionally rendered)
                if st.button("💬 Add a Comment", key=f"comment_{post_id}"):
                    st.text_input("Write a comment...", key=f"comment_input_{post_id}")
                st.markdown("</div>", unsafe_allow_html=True)
else:
        st.write("No posts found.")


# Spacing between sections
st.write("")
st.write("")
st.write("### 📝 Create or Manage Posts")

# New Post Section
st.markdown("#### ✍️ Create a New Post")
with st.form(key="create_post"):
    student_id = st.text_input("Student ID", placeholder="Enter your Student ID")
    content = st.text_area("Content", placeholder="What's on your mind?")
    post_date = st.date_input("Post Date", value=datetime.now().date())
    category = st.text_input("Category", placeholder="Enter a category (e.g., News, Updates)")
    submit_button = st.form_submit_button(label="Post")

    if submit_button:
        post_data = {
            "StudentId": student_id,
            "Content": content,
            "PostDate": str(post_date),
            "Category": category,
        }
        response = requests.post(BASE_URL, json=post_data)
        if response.status_code == 201:
            st.success("Your post has been created successfully!")
        else:
            st.error("Failed to create the post. Please try again.")

# Delete Post Section
st.markdown("#### 🗑️ Delete a Post")
post_id_to_delete = st.number_input("Enter the Post ID to delete", min_value=1, step=1)
if st.button("Delete Post"):
    response = requests.delete(f"{BASE_URL}/{post_id_to_delete}")
    if response.status_code == 200:
        st.success(f"Post {post_id_to_delete} has been deleted successfully!")
    else:
        st.error("Failed to delete the post. Please try again.")
