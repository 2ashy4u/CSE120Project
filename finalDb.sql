-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 08, 2022 at 03:20 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `usersdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `answer`
--

CREATE TABLE `answer` (
  `answer` varchar(150) DEFAULT NULL,
  `points` int(11) DEFAULT NULL,
  `feedback` varchar(150) DEFAULT NULL,
  `employee_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `question_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `idcourses` int(11) NOT NULL,
  `courseTitle` varchar(25) DEFAULT NULL,
  `courseDes` varchar(300) DEFAULT NULL,
  `courseLink` varchar(150) DEFAULT NULL,
  `courseFeedback` varchar(150) DEFAULT NULL,
  `courseTime` varchar(30) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `startDate` varchar(15) DEFAULT NULL,
  `endDate` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `employee_course`
--

CREATE TABLE `employee_course` (
  `employee_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `manager_id` int(11) DEFAULT NULL,
  `answer` varchar(150) DEFAULT NULL,
  `feedback` varchar(150) DEFAULT NULL,
  `progress` decimal(5,2) DEFAULT 0.00
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `question`
--

CREATE TABLE `question` (
  `questionId` int(11) NOT NULL,
  `data` varchar(500) DEFAULT NULL,
  `maxPoints` int(11) DEFAULT NULL,
  `link` varchar(150) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(20) NOT NULL,
  `firstname` varchar(50) DEFAULT NULL,
  `lastname` varchar(30) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `isManager` char(1) NOT NULL,
  `isSupManager` char(1) NOT NULL,
  `password` varchar(40) NOT NULL,
  `manager_id` int(11) DEFAULT NULL,
  `department` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `firstname`, `lastname`, `email`, `isManager`, `isSupManager`, `password`, `manager_id`, `department`) VALUES
(1, 'Clark', 'Super', 'supermanager@wdc.com', 'Y', 'Y', '1234', NULL, ''),
(2, 'Jane', 'Manager', 'manager1@wdc.com', 'Y', 'Y', '1234', 1, 'department 1'),
(3, 'John', 'Trainer', 'manager2@wdc.com', 'Y', 'N', '1234', 1, 'department 2'),
(4, 'Alan', 'Employee', 'employee1@wdc.com', 'N', 'N', '1234', 2, 'department 1'),
(5, 'William', 'Trainee', 'employee2@wdc.com', 'N', 'N', '1234', 2, 'department 1'),
(6, 'Gary', 'Recruit', 'employee3@wdc.com', 'N', 'N', '1234', 2, 'department 1'),
(7, 'Rose', 'Student', 'employee4@wdc.com', 'N', 'N', '1234', 3, 'department 2'),
(8, 'Mary', 'Newhire', 'employee5@wdc.com', 'N', 'N', '1234', 3, 'department 2'),
(9, 'Noah', 'Intern', 'employee6@wdc.com', 'N', 'N', '1234', 3, 'department 2');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `answer`
--
ALTER TABLE `answer`
  ADD PRIMARY KEY (`employee_id`,`course_id`,`question_id`),
  ADD KEY `course_id` (`course_id`),
  ADD KEY `question_id` (`question_id`);

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`idcourses`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `employee_course`
--
ALTER TABLE `employee_course`
  ADD PRIMARY KEY (`employee_id`,`course_id`),
  ADD KEY `course_id` (`course_id`),
  ADD KEY `manager_id` (`manager_id`);

--
-- Indexes for table `question`
--
ALTER TABLE `question`
  ADD PRIMARY KEY (`questionId`),
  ADD KEY `course_id` (`course_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD KEY `manager_id` (`manager_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `course`
--
ALTER TABLE `course`
  MODIFY `idcourses` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `question`
--
ALTER TABLE `question`
  MODIFY `questionId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=83;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `answer`
--
ALTER TABLE `answer`
  ADD CONSTRAINT `answer_ibfk_2` FOREIGN KEY (`employee_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `course`
--
ALTER TABLE `course`
  ADD CONSTRAINT `course_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `employee_course`
--
ALTER TABLE `employee_course`
  ADD CONSTRAINT `employee_course_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `employee_course_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `course` (`idcourses`),
  ADD CONSTRAINT `employee_course_ibfk_3` FOREIGN KEY (`manager_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `question`
--
ALTER TABLE `question`
  ADD CONSTRAINT `question_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`idcourses`);

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`manager_id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
