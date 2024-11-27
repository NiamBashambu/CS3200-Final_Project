
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

DROP DATABASE IF EXISTS coconnect;

CREATE DATABASE IF NOT EXISTS coconnect ;

grant all privileges on coconnect.* to 'root'@'%';
flush privileges;

USE coconnect;



-- Create the CoOp Advisor table
CREATE TABLE CoOpAdvisor (
    CoopAdvisorID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Department VARCHAR(50),
    Field VARCHAR(50)
);

-- Create the Student table
CREATE TABLE Student (
    StudentId INT AUTO_INCREMENT PRIMARY KEY,
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
    ResumeId INT AUTO_INCREMENT PRIMARY KEY,
    StudentId INT,
    Content TEXT,
    LastUpdated DATE,
    FOREIGN KEY (StudentId) REFERENCES Student(StudentId)
);

-- Create the Student Searching table
CREATE TABLE StudentSearching (
    StudentId INT AUTO_INCREMENT PRIMARY KEY ,
    ResumeId INT,
    EmployStatus VARCHAR(20),
    FOREIGN KEY (StudentId) REFERENCES Student(StudentId),
    FOREIGN KEY (ResumeId) REFERENCES Resume(ResumeId)
);

-- Create the Student Exploring Fields table
CREATE TABLE StudentExploringFields (
    StudentId INT AUTO_INCREMENT PRIMARY KEY ,
    Interest VARCHAR(50),
    FOREIGN KEY (StudentId) REFERENCES Student(StudentId)
);

-- Create the Posts table
CREATE TABLE Posts (
    PostId INT AUTO_INCREMENT PRIMARY KEY,
    StudentId INT,
    Content TEXT,
    PostDate DATE,
    Category VARCHAR(50),
    FOREIGN KEY (StudentId) REFERENCES Student(StudentId)
);

-- Create the Company table
CREATE TABLE Company (
    CompanyId INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    State VARCHAR(50),
    City VARCHAR(50)
);

-- Create the Job Listing table
CREATE TABLE JobListing (
    JobId INT AUTO_INCREMENT PRIMARY KEY,
    Position VARCHAR(100),
    CompanyId INT,
    Department VARCHAR(50),
    Description TEXT,
    Location VARCHAR(100),
    PostDate DATE,
    FOREIGN KEY (CompanyId) REFERENCES Company(CompanyId)
);


-- Create the Notification table
CREATE TABLE Notification (
    NotifId INT AUTO_INCREMENT PRIMARY KEY,
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
    EmployerId INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    Phone VARCHAR(15),
    CompanyId INT,
    FOREIGN KEY (CompanyId) REFERENCES Company(CompanyId)
);


-- Insert CoOp Advisors
INSERT INTO CoOpAdvisor (Name, Department, Field)
SELECT
    CONCAT('Advisor_', FLOOR(RAND() * 1000)),
    CASE FLOOR(RAND() * 4)
        WHEN 0 THEN 'CS'
        WHEN 1 THEN 'ECE'
        WHEN 2 THEN 'ME'
        WHEN 3 THEN 'Bio'
    END,
    CASE FLOOR(RAND() * 4)
        WHEN 0 THEN 'AI'
        WHEN 1 THEN 'Robotics'
        WHEN 2 THEN 'Networking'
        WHEN 3 THEN 'Data Science'
    END
FROM
    (SELECT 1 FROM information_schema.columns LIMIT 30) AS tmp;


-- Insert Students
INSERT INTO Student (Name, Email, Phone, YOG, Major, Advisor)
SELECT
    CONCAT('Student_', FLOOR(RAND() * 10000)),
    CONCAT('student_', FLOOR(RAND() * 10000), '@example.com'),
    CONCAT('+1', FLOOR(RAND() * 9000000000) + 1000000000),
    2024 + FLOOR(RAND() * 4),
    CASE FLOOR(RAND() * 4)
        WHEN 0 THEN 'CS'
        WHEN 1 THEN 'ECE'
        WHEN 2 THEN 'ME'
        WHEN 3 THEN 'Bio'
    END,
    FLOOR(RAND() * 100) + 1
FROM
    (SELECT 1 FROM information_schema.columns LIMIT 100) AS tmp;



-- Insert Resumes
INSERT INTO Resume (StudentId, Content, LastUpdated)
SELECT
    FLOOR(RAND() * 1000) + 1,
    CONCAT('Resume content for student ', FLOOR(RAND() * 1000) + 1),
    DATE_ADD('2023-01-01', INTERVAL FLOOR(RAND() * 365) DAY)
FROM
    (SELECT 1 FROM information_schema.columns LIMIT 100) AS tmp;


-- Insert Student Exploring Fields
INSERT INTO StudentExploringFields (StudentId, Interest)
SELECT
    FLOOR(RAND() * 1000) + 1,
    CASE FLOOR(RAND() * 4)
        WHEN 0 THEN 'AI'
        WHEN 1 THEN 'Robotics'
        WHEN 2 THEN 'Networking'
        WHEN 3 THEN 'Data Science'
    END
FROM
    (SELECT 1 FROM information_schema.columns LIMIT 100) AS tmp;


-- Insert Student Searching Entries
INSERT INTO StudentSearching (StudentId, ResumeId, EmployStatus)
SELECT
    FLOOR(RAND() * 1000) + 1,
    FLOOR(RAND() * 1000) + 1,
    CASE FLOOR(RAND() * 3)
        WHEN 0 THEN 'Searching'
        WHEN 1 THEN 'Not Searching'
        WHEN 2 THEN 'Employed'
    END
FROM
    (SELECT 1 FROM information_schema.columns LIMIT 100) AS tmp;
-- Insert Posts
INSERT INTO Posts (StudentId, Content, PostDate, Category)
SELECT
    FLOOR(RAND() * 1000) + 1,
    CONCAT('Post content ', FLOOR(RAND() * 1000) + 1),
    DATE_ADD('2023-01-01', INTERVAL FLOOR(RAND() * 365) DAY),
    CASE FLOOR(RAND() * 3)
        WHEN 0 THEN 'Announcement'
        WHEN 1 THEN 'Job Opportunity'
        WHEN 2 THEN 'Event'
    END
FROM
    (SELECT 1 FROM information_schema.columns LIMIT 100) AS tmp;

-- Insert Companies
INSERT INTO Company (Name, State, City)
SELECT
    CONCAT('Company_', FLOOR(RAND() * 100)),
    CASE FLOOR(RAND() * 4)
        WHEN 0 THEN 'CA'
        WHEN 1 THEN 'NY'
        WHEN 2 THEN 'TX'
        WHEN 3 THEN 'FL'
    END,
    CASE FLOOR(RAND() * 4)
        WHEN 0 THEN 'Los Angeles'
        WHEN 1 THEN 'New York'
        WHEN 2 THEN 'Austin'
        WHEN 3 THEN 'Miami'
    END
FROM
    (SELECT 1 FROM information_schema.columns LIMIT 100) AS tmp;

-- Insert Job Listings
INSERT INTO JobListing (Position, CompanyId, Department, Description, Location, PostDate)
SELECT
    CONCAT('Position ', FLOOR(RAND() * 100)),
    FLOOR(RAND() * 100) + 1,
    CASE FLOOR(RAND() * 4)
        WHEN 0 THEN 'CS'
        WHEN 1 THEN 'ECE'
        WHEN 2 THEN 'ME'
        WHEN 3 THEN 'Bio'
    END,
    CONCAT('Job Description for position ', FLOOR(RAND() * 100)),
    CASE FLOOR(RAND() * 4)
        WHEN 0 THEN 'Los Angeles'
        WHEN 1 THEN 'New York'
        WHEN 2 THEN 'Austin'
        WHEN 3 THEN 'Miami'
    END,
    DATE_ADD('2023-01-01', INTERVAL FLOOR(RAND() * 365) DAY)
FROM
    (SELECT 1 FROM information_schema.columns LIMIT 50) AS tmp;
-- Insert Notifications
INSERT INTO Notification (PostId, JobId, StudentId, TimeStamp, Content)
SELECT
    FLOOR(RAND() * 1000) + 1,
    FLOOR(RAND() * 500) + 1,
    FLOOR(RAND() * 1000) + 1,
    NOW(),
    CONCAT('Notification content for student ', FLOOR(RAND() * 1000) + 1)
FROM
    (SELECT 1 FROM information_schema.columns LIMIT 100) AS tmp;

-- Insert Employers
INSERT INTO Employer (Name, Email, Phone, CompanyId)
SELECT
    CONCAT('Employer_', FLOOR(RAND() * 100)),
    CONCAT('employer_', FLOOR(RAND() * 10000), '@example.com'),
    CONCAT('+1', FLOOR(RAND() * 9000000000) + 1000000000),
    FLOOR(RAND() * 100) + 1
FROM
    (SELECT 1 FROM information_schema.columns LIMIT 50) AS tmp;




SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;