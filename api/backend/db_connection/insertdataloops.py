import random
import string
from datetime import datetime, timedelta
from backend.db_connection import db


def populate_database():
    cursor = db.connection.cursor()

    # Utility functions
    def random_string(length=8):
        return ''.join(random.choices(string.ascii_letters, k=length))

    def random_email(name):
        return f"{name.lower()}@example.com"

    def random_date(start, end):
        delta = end - start
        random_days = random.randint(0, delta.days)
        return start + timedelta(days=random_days)

    try:
        # Insert CoOp Advisors
        advisors = [
            (
                i,
                random_string(6),
                random.choice(["CS", "ECE", "ME", "Bio"]),
                random.choice(["AI", "Robotics", "Networking", "Data Science"]),
            )
            for i in range(1, 21)  # 20 advisors
        ]
        cursor.executemany(
            "INSERT INTO CoOpAdvisor (CoopAdvisorID, Name, Department, Field) VALUES (%s, %s, %s, %s)",
            advisors,
        )
        db.connection.commit()

        # Insert Students
        students = [
            (
                random_string(6),
                random_email(random_string(6)),
                ''.join(random.choices(string.digits, k=10)),
                random.randint(2024, 2027),
                random.choice(["CS", "ECE", "ME", "Bio"]),
                random.randint(1, 20),
            )
            for _ in range(200)  # 200 students
        ]
        cursor.executemany(
            "INSERT INTO Student (Name, Email, Phone, YOG, Major, Advisor) VALUES (%s, %s, %s, %s, %s, %s)",
            students,
        )
        db.connection.commit()

        # Insert Resumes
        resumes = [
            (
                i,
                f"Resume content for student {i}",
                random_date(datetime(2023, 1, 1), datetime(2024, 1, 1)),
            )
            for i in range(1, 201)  # One resume per student
        ]
        cursor.executemany(
            "INSERT INTO Resume (ResumeId, StudentId, Content, LastUpdated) VALUES (%s, %s, %s)",
            resumes,
        )
        db.connection.commit()

        # Insert Student Searching
        student_searching = [
            (i, i, random.choice(["Searching", "Not Searching", "Employed"]))
            for i in range(1, 201)  # One search entry per student
        ]
        cursor.executemany(
            "INSERT INTO StudentSearching (StudentId, ResumeId, EmployStatus) VALUES (%s, %s, %s)",
            student_searching,
        )
        db.connection.commit()

        # Insert Student Exploring Fields
        exploring_fields = [
            (i, random.choice(["AI", "Robotics", "Networking", "Data Science"]))
            for i in range(1, 201)  # One interest per student
        ]
        cursor.executemany(
            "INSERT INTO StudentExploringFields (StudentId, Interest) VALUES (%s, %s)",
            exploring_fields,
        )
        db.connection.commit()

        # Insert Posts
        posts = [
            (
                i,
                random.randint(1, 200),
                f"Post content {i}",
                random_date(datetime(2023, 1, 1), datetime(2024, 1, 1)),
                random.choice(["Announcement", "Job Opportunity", "Event"]),
            )
            for i in range(1, 301)  # 300 posts
        ]
        cursor.executemany(
            "INSERT INTO Posts (PostId, StudentId, Content, PostDate, Category) VALUES (%s, %s, %s, %s, %s)",
            posts,
        )
        db.connection.commit()

        # Insert Companies
        companies = [
            (
                i,
                f"Company_{i}",
                random.choice(["CA", "NY", "TX", "FL"]),
                random.choice(["Los Angeles", "New York", "Austin", "Miami"]),
            )
            for i in range(1, 51)  # 50 companies
        ]
        cursor.executemany(
            "INSERT INTO Company (CompanyId, Name, State, City) VALUES (%s, %s, %s, %s)",
            companies,
        )
        db.connection.commit()

        print("Database populated successfully!")

    except Exception as e:
        print(f"Error while populating database: {e}")
        db.connection.rollback()


# To use the function, call it in the Flask app context
# Example usage:
# with app.app_context():
#     populate_database()
