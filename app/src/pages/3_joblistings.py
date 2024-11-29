import logging
import streamlit as st
import requests
from datetime import datetime

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

BASE_URL = "http://web-api:4000/j"

# Set page layout to wide
st.set_page_config(layout="wide", page_title="Job Listings", page_icon="💼")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f4f7fb;
    }
    .job-container {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease-in-out;
    }
    .job-container:hover {
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        transform: translateY(-5px);
    }
    .job-header {
        font-weight: 600;
        font-size: 18px;
        color: #333;
        margin-bottom: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .job-header span {
        font-size: 14px;
        color: #888;
    }
    .job-content {
        font-size: 16px;
        color: #555;
        line-height: 1.8;
        margin-bottom: 20px;
    }
    .job-footer {
        font-size: 14px;
        color: #666;
        display: flex;
        justify-content: flex-end;
    }
    .add-job-btn {
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
    .add-job-btn:hover {
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
    </style>
    """,
    unsafe_allow_html=True,
)