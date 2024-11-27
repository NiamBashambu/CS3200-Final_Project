
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






SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;