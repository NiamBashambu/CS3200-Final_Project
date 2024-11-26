import random
import string
from datetime import datetime, timedelta
from backend.db_connection import db
from flask import Blueprint




cursor = db.cursor()

# Utility functions
def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_email(name):
    return f"{name.lower()}@example.com"

def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

# Insert CoOp Advisors
advisors = []
for i in range(1, 21):  # 20 advisors
    name = random_string(6)
    department = random.choice(["CS", "ECE", "ME", "Bio"])
    field = random.choice(["AI", "Robotics", "Networking", "Data Science"])
    advisors.append((i, name, department, field))
cursor.executemany(
    "INSERT INTO CoOpAdvisor (CoopAdvisorID, Name, Department, Field) VALUES (%s, %s, %s, %s)",
    advisors
)

# Insert Students
students = []
for i in range(1, 201):  # 200 students
    name = random_string(6)
    email = random_email(name)
    phone = ''.join(random.choices(string.digits, k=10))
    yog = random.randint(2024, 2027)
    major = random.choice(["CS", "ECE", "ME", "Bio"])
    advisor_id = random.randint(1, 20)
    students.append((name, email, phone, yog, major, advisor_id))
cursor.executemany(
    "INSERT INTO Student (Name, Email, Phone, YOG, Major, Advisor) VALUES (%s, %s, %s, %s, %s, %s)",
    students
)

# Insert Resumes
resumes = []
for i in range(1, 201):  # One resume per student
    content = f"Resume content for student {i}"
    last_updated = random_date(datetime(2023, 1, 1), datetime(2024, 1, 1))
    resumes.append((i, content, last_updated))
cursor.executemany(
    "INSERT INTO Resume (ResumeId, StudentId, Content, LastUpdated) VALUES (%s, %s, %s)",
    resumes
)

# Insert Student Searching
student_searching = []
for i in range(1, 201):  # One search entry per student
    employ_status = random.choice(["Searching", "Not Searching", "Employed"])
    student_searching.append((i, i, employ_status))
cursor.executemany(
    "INSERT INTO StudentSearching (StudentId, ResumeId, EmployStatus) VALUES (%s, %s, %s)",
    student_searching
)

# Insert Student Exploring Fields
exploring_fields = []
for i in range(1, 201):  # One interest per student
    interest = random.choice(["AI", "Robotics", "Networking", "Data Science"])
    exploring_fields.append((i, interest))
cursor.executemany(
    "INSERT INTO StudentExploringFields (StudentId, Interest) VALUES (%s, %s)",
    exploring_fields
)

# Insert Posts
posts = []
for i in range(1, 301):  # 300 posts
    student_id = random.randint(1, 200)
    content = f"Post content {i}"
    post_date = random_date(datetime(2023, 1, 1), datetime(2024, 1, 1))
    category = random.choice(["Announcement", "Job Opportunity", "Event"])
    posts.append((i, student_id, content, post_date, category))
cursor.executemany(
    "INSERT INTO Posts (PostId, StudentId, Content, PostDate, Category) VALUES (%s, %s, %s, %s, %s)",
    posts
)

# Insert Companies
companies = []
for i in range(1, 51):  # 50 companies
    name = f"Company_{i}"
    state = random.choice(["CA", "NY", "TX", "FL"])
    city = random.choice(["Los Angeles", "New York", "Austin", "Miami"])
    companies.append((i, name, state, city))
cursor.executemany(
    "INSERT INTO Company (CompanyId, Name, State, City) VALUES (%s, %s, %s, %s)",
    companies
)