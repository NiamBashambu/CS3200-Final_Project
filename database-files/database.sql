

DROP DATABASE IF EXISTS `coconnect`;

CREATE DATABASE IF NOT EXISTS `coconnect`;
USE `coconnect`;



-- Create the CoOp Advisor table
CREATE TABLE CoOpAdvisor (
    CoopAdvisorID INT PRIMARY KEY,
    Name VARCHAR(100),
    Department VARCHAR(50),
    Field VARCHAR(50)
);

-- Create the Student table
CREATE TABLE Student (
    StudentId INT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    Phone VARCHAR(15),
    YOG YEAR, -- Year of Graduation
    Major VARCHAR(50),
    Advisor INT,
    FOREIGN KEY (Advisor) REFERENCES CoOpAdvisor(CoopAdvisorID)
);

-- Create the Resume table
CREATE TABLE Resume (
    ResumeId INT PRIMARY KEY,
    StudentId INT,
    Content TEXT,
    LastUpdated DATE,
    FOREIGN KEY (StudentId) REFERENCES Student(StudentId)
);

-- Create the Student Searching table
CREATE TABLE StudentSearching (
    StudentId INT PRIMARY KEY ,
    ResumeId INT,
    EmployStatus VARCHAR(20),
    FOREIGN KEY (StudentId) REFERENCES Student(StudentId),
    FOREIGN KEY (ResumeId) REFERENCES Resume(ResumeId)
);

-- Create the Student Exploring Fields table
CREATE TABLE StudentExploringFields (
    StudentId INT PRIMARY KEY ,
    Interest VARCHAR(50),
    FOREIGN KEY (StudentId) REFERENCES Student(StudentId)
);

-- Create the Posts table
CREATE TABLE Posts (
    PostId INT PRIMARY KEY,
    StudentId INT,
    Content TEXT,
    PostDate DATE,
    Category VARCHAR(50),
    FOREIGN KEY (StudentId) REFERENCES Student(StudentId)
);

-- Create the Company table
CREATE TABLE Company (
    CompanyId INT PRIMARY KEY,
    Name VARCHAR(100),
    State VARCHAR(50),
    City VARCHAR(50)
);
-- Create the Job Listing table
CREATE TABLE JobListing (
    JobId INT PRIMARY KEY,
    Position VARCHAR(100),
    CompanyId INT,
    Department VARCHAR(50),
    Description TEXT,
    FOREIGN KEY (CompanyId) REFERENCES Company(CompanyId)
);


-- Create the Notification table
CREATE TABLE Notification (
    NotifId INT PRIMARY KEY,
    PostId INT,
    JobId INT,
    StudentId INT,
    TimeStamp DATETIME,
    Content TEXT,
    FOREIGN KEY (PostId) REFERENCES Posts(PostId),
    FOREIGN KEY (JobId) REFERENCES JobListing(JobId),
    FOREIGN KEY (StudentId) REFERENCES Student(StudentId)
);




-- Create the Employer table
CREATE TABLE Employer (
    EmployerId INT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    Phone VARCHAR(15),
    CompanyId INT,
    FOREIGN KEY (CompanyId) REFERENCES Company(CompanyId)
);



-- Insert sample data into CoOpAdvisor table
INSERT INTO CoOpAdvisor (CoopAdvisorID, Name, Department, Field)
VALUES
(1, 'Dr. Emily Smith', 'Computer Science', 'Artificial Intelligence'),
(2, 'Dr. John Doe', 'Mechanical Engineering', 'Robotics');

-- Insert sample data into Student table
INSERT INTO Student (StudentId, Name, Email, Phone, YOG, Major, Advisor)
VALUES
(101, 'Alice Johnson', 'alice.johnson@example.com', '123-456-7890', 2025, 'Computer Science', 1),
(102, 'Bob Brown', 'bob.brown@example.com', '987-654-3210', 2024, 'Mechanical Engineering', 2);

-- Insert sample data into Resume table
INSERT INTO Resume (ResumeId, StudentId, Content, LastUpdated)
VALUES
(201, 101, 'Alice\'s resume content...', '2024-10-15'),
(202, 102, 'Bob\'s resume content...', '2024-09-10');

-- Insert sample data into StudentSearching table
INSERT INTO StudentSearching (StudentId, ResumeId, EmployStatus)
VALUES
(101, 201, 'Seeking Internship'),
(102, 202, 'Seeking Full-Time');

-- Insert sample data into StudentExploringFields table
INSERT INTO StudentExploringFields (StudentId, Interest)
VALUES
(101, 'Machine Learning'),
(102, 'CAD Design');

-- Insert sample data into Posts table
INSERT INTO Posts (PostId, StudentId, Content, PostDate, Category)
VALUES
(301, 101, 'Excited to start applying for AI internships!', '2024-11-01', 'Career Updates'),
(302, 102, 'Looking for robotics opportunities!', '2024-11-02', 'Job Hunt');

-- Insert sample data into Company table
INSERT INTO Company (CompanyId, Name, State, City)
VALUES
(401, 'Tech Innovators', 'California', 'San Francisco'),
(402, 'Robotics World', 'New York', 'New York City');

-- Insert sample data into JobListing table
INSERT INTO JobListing (JobId, Position, CompanyId, Department, Description)
VALUES
(501, 'AI Engineer Intern', 401, 'AI Development', 'Internship for AI/ML projects'),
(502, 'Robotics Engineer', 402, 'Engineering', 'Full-time role in robotics team');

-- Insert sample data into Notification table
INSERT INTO Notification (NotifId, PostId, JobId, StudentId, TimeStamp, Content)
VALUES
(601, 301, 501, 101, '2024-11-03 10:00:00', 'Check out this AI internship opportunity!'),
(602, 302, 502, 102, '2024-11-04 12:30:00', 'Robotics role you might like!');

-- Insert sample data into Employer table
INSERT INTO Employer (EmployerId, Name, Email, Phone, CompanyId)
VALUES
(701, 'Sarah Green', 'sarah.green@techinnovators.com', '123-789-4561', 401),
(702, 'Mark Wilson', 'mark.wilson@roboticsworld.com', '321-654-9872', 402);

