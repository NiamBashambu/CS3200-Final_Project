import logging
import streamlit as st
import requests

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Define the base URL of your Flask API (adjust if necessary)
BASE_URL = "http://web-api:4000/posts"
# Set page layout to wide
st.set_page_config(layout='wide')

# Create Sidebar Navigation Links
from modules.nav import SideBarLinks
SideBarLinks()

# Title for the Streamlit app
st.title('Facebook-like Post Feed')
st.write('')
st.write('')

# Display Section Title for Posts
st.write('### Posts Feed')

# Fetch Posts Automatically from the API
posts = requests.get(f'{BASE_URL}')  # Fetch posts from the API

if posts:
    for post in posts:
        post_id = post['PostId']
        student_id = post['StudentId']
        content = post['Content']
        post_date = post['PostDate']
        category = post['Category']

        # Facebook-like post design
        with st.container():
            # Post Header: Student Info and Post Category
            st.markdown(f"#### Post by Student {student_id} ({category})")
            st.write(f"**Date**: {post_date}")
            st.write(f"**Post ID**: {post_id}")

            # Post Content
            st.write(f"**Content**: {content}")

            # Adding a nice separation between posts
            st.write("---")

            # Actions: Like, Comment, Share (optional)
            col1, col2, col3 = st.columns([1, 3, 1])
            with col1:
                if st.button('Like', key=f"like_{post_id}"):
                    st.success("Liked!")
            with col2:
                if st.button('Comment', key=f"comment_{post_id}"):
                    st.text_input(f"Comment on Post {post_id}")
            with col3:
                if st.button('Share', key=f"share_{post_id}"):
                    st.success("Shared!")

else:
    st.write("No posts found.")

# Spacing between sections
st.write('')
st.write('')
st.write('### New Post Management')

# Button for Creating a New Post (this part remains unchanged)
if st.button('Create New Post', type='primary', use_container_width=True):
    logger.info("User clicked on Create New Post")
    st.write("#### Create a New Post")
    
    # Form to create a new post
    with st.form(key="create_post"):
        student_id = st.text_input("Student ID")
        content = st.text_area("Content")
        post_date = st.date_input("Post Date")
        category = st.text_input("Category")
        
        submit_button = st.form_submit_button(label="Create Post")
        
        if submit_button:
            post_data = {
                "StudentId": student_id,
                "Content": content,
                "PostDate": str(post_date),
                "Category": category
            }
            response = requests.post(f'{BASE_URL}', json=post_data)
            if response.status_code == 201:
                st.success("Post created successfully!")
            else:
                st.error("Failed to create the post.")

# Button for Deleting a Post (this part remains unchanged)
if st.button('Delete a Post', type='primary', use_container_width=True):
    logger.info("User clicked on Delete a Post")
    post_id_to_delete = st.number_input("Enter Post ID to delete", min_value=1, step=1)
    
    delete_button = st.button("Delete Post")
    if delete_button:
        response = requests.delete(f"{BASE_URL}/{post_id_to_delete}")
        if response.status_code == 200:
            st.success(f"Post {post_id_to_delete} deleted successfully!")
        else:
            st.error("Failed to delete the post.")
