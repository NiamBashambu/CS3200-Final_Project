

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


DELIMITER //
CREATE PROCEDURE PopulateCoOpAdvisor()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 50 DO
        INSERT INTO CoOpAdvisor (CoopAdvisorID, Name, Department, Field)
        VALUES (i, CONCAT('Dr. Advisor ', i),
            CASE
                WHEN i % 3 = 0 THEN 'Computer Science'
                WHEN i % 3 = 1 THEN 'Mechanical Engineering'
                ELSE 'Electrical Engineering'
            END,
            CASE
                WHEN i % 3 = 0 THEN 'Artificial Intelligence'
                WHEN i % 3 = 1 THEN 'Robotics'
                ELSE 'Power Systems'
            END);
        SET i = i + 1;
    END WHILE;
END;
//
DELIMITER ;
CALL PopulateCoOpAdvisor();

DELIMITER //
CREATE PROCEDURE PopulateStudents()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 500 DO
        INSERT INTO Student (StudentId, Name, Email, Phone, YOG, Major, Advisor)
        VALUES (i, CONCAT('Student ', i), CONCAT('student', i, '@example.com'),
            CONCAT('123-', LPAD(i MOD 1000, 3, '0'), '-', LPAD((i * 17) MOD 10000, 4, '0')),
            2024 + (i MOD 3),
            CASE
                WHEN i % 3 = 0 THEN 'Computer Science'
                WHEN i % 3 = 1 THEN 'Mechanical Engineering'
                ELSE 'Electrical Engineering'
            END,
            (i MOD 50) + 1);
        SET i = i + 1;
    END WHILE;
END;
//
DELIMITER ;
CALL PopulateStudents();


DELIMITER //
CREATE PROCEDURE PopulateResumes()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 500 DO
        INSERT INTO Resume (ResumeId, StudentId, Content, LastUpdated)
        VALUES (i, i, CONCAT('Resume content for Student ', i),
            DATE_SUB(CURDATE(), INTERVAL (i MOD 100) DAY));
        SET i = i + 1;
    END WHILE;
END;
//
DELIMITER ;
CALL PopulateResumes();


DELIMITER //
CREATE PROCEDURE PopulateStudentSearching()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 500 DO
        INSERT INTO StudentSearching (StudentId, ResumeId, EmployStatus)
        VALUES (i, i,
            CASE
                WHEN i % 2 = 0 THEN 'Seeking Internship'
                ELSE 'Seeking Full-Time'
            END);
        SET i = i + 1;
    END WHILE;
END;
//
DELIMITER ;
CALL PopulateStudentSearching();


DELIMITER //
CREATE PROCEDURE PopulateStudentExploringFields()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 500 DO
        INSERT INTO StudentExploringFields (StudentId, Interest)
        VALUES (i,
            CASE
                WHEN i % 4 = 0 THEN 'Machine Learning'
                WHEN i % 4 = 1 THEN 'CAD Design'
                WHEN i % 4 = 2 THEN 'Networking'
                ELSE 'Embedded Systems'
            END);
        SET i = i + 1;
    END WHILE;
END;
//
DELIMITER ;
CALL PopulateStudentExploringFields();



DELIMITER //
CREATE PROCEDURE PopulateCompanies()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 100 DO
        INSERT INTO Company (CompanyId, Name, State, City)
        VALUES (i, CONCAT('Company ', i),
            CASE
                WHEN i % 3 = 0 THEN 'California'
                WHEN i % 3 = 1 THEN 'New York'
                ELSE 'Texas'
            END,
            CASE
                WHEN i % 3 = 0 THEN 'San Francisco'
                WHEN i % 3 = 1 THEN 'New York City'
                ELSE 'Austin'
            END);
        SET i = i + 1;
    END WHILE;
END;
//
DELIMITER ;
CALL PopulateCompanies();


DELIMITER //
CREATE PROCEDURE PopulateJobListings()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 500 DO
        INSERT INTO JobListing (JobId, Position, CompanyId, Department, Description)
        VALUES (i, CONCAT('Position ', i),
            (i MOD 100) + 1,
            CASE
                WHEN i % 3 = 0 THEN 'AI Development'
                WHEN i % 3 = 1 THEN 'Engineering'
                ELSE 'Marketing'
            END,
            CONCAT('Description for Position ', i));
        SET i = i + 1;
    END WHILE;
END;
//
DELIMITER ;
CALL PopulateJobListings();


DELIMITER //
CREATE PROCEDURE PopulateNotifications()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 500 DO
        INSERT INTO Notification (NotifId, PostId, JobId, StudentId, TimeStamp, Content)
        VALUES (i, i, (i MOD 500) + 1, i,
            DATE_ADD('2024-01-01 00:00:00', INTERVAL i HOUR),
            CONCAT('Notification content for Post ', i));
        SET i = i + 1;
    END WHILE;
END;
//
DELIMITER ;
CALL PopulateNotifications();


DELIMITER //
CREATE PROCEDURE PopulateEmployers()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 100 DO
        INSERT INTO Employer (EmployerId, Name, Email, Phone, CompanyId)
        VALUES (i, CONCAT('Employer ', i),
            CONCAT('employer', i, '@company', i, '.com'),
            CONCAT('987-', LPAD(i MOD 1000, 3, '0'), '-', LPAD((i * 19) MOD 10000, 4, '0')),
            (i MOD 100) + 1);
        SET i = i + 1;
    END WHILE;
END;
//
DELIMITER ;
CALL PopulateEmployers();


DELIMITER //
CREATE PROCEDURE PopulatePosts()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 500 DO
        INSERT INTO Posts (PostId, StudentId, Content, PostDate, Category)
        VALUES (i, i, CONCAT('Post content for Student ', i),
            DATE_SUB(CURDATE(), INTERVAL (i MOD 30) DAY),
            CASE
                WHEN i % 2 = 0 THEN 'Career Updates'
                ELSE 'Job Hunt'
            END);
        SET i = i + 1;
    END WHILE;
END;
//
DELIMITER ;
CALL PopulatePosts();