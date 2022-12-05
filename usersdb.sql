-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 04, 2022 at 10:55 PM
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

--
-- Dumping data for table `answer`
--

INSERT INTO `answer` (`answer`, `points`, `feedback`, `employee_id`, `course_id`, `question_id`) VALUES
('sdvgbgdfn', 0, 'wcwec', 4, 14, 64),
('asdce', 0, 'wefcwe', 4, 14, 65),
('saww', 0, 'wacef', 4, 14, 66),
(NULL, NULL, NULL, 4, 14, 67),
(NULL, NULL, NULL, 4, 14, 69),
(NULL, NULL, NULL, 4, 14, 74),
(NULL, NULL, NULL, 4, 14, 75),
(NULL, NULL, NULL, 4, 15, 76),
(NULL, NULL, NULL, 4, 15, 77),
(NULL, NULL, NULL, 5, 14, 64),
(NULL, NULL, NULL, 5, 14, 65),
(NULL, NULL, NULL, 5, 14, 66),
(NULL, NULL, NULL, 5, 14, 67),
(NULL, NULL, NULL, 5, 14, 69),
(NULL, NULL, NULL, 5, 14, 74),
(NULL, NULL, NULL, 5, 14, 75),
(NULL, NULL, NULL, 6, 14, 64),
(NULL, NULL, NULL, 6, 14, 65),
(NULL, NULL, NULL, 6, 14, 66),
(NULL, NULL, NULL, 6, 14, 67),
(NULL, NULL, NULL, 6, 14, 69),
(NULL, NULL, NULL, 6, 14, 74),
(NULL, NULL, NULL, 6, 14, 75),
(NULL, NULL, NULL, 6, 15, 76),
(NULL, NULL, NULL, 6, 15, 77);

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `idcourses` int(11) NOT NULL,
  `courseTitle` varchar(25) DEFAULT NULL,
  `courseDes` varchar(150) DEFAULT NULL,
  `courseLink` varchar(50) DEFAULT NULL,
  `courseFeedback` varchar(150) DEFAULT NULL,
  `courseTime` varchar(30) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `startDate` varchar(15) DEFAULT NULL,
  `endDate` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`idcourses`, `courseTitle`, `courseDes`, `courseLink`, `courseFeedback`, `courseTime`, `user_id`, `startDate`, `endDate`) VALUES
(5, NULL, 'Is this a course?', NULL, NULL, 'now', 1, NULL, NULL),
(6, NULL, 'hahahaha', NULL, NULL, 'now', 1, NULL, NULL),
(7, 'asDqwd', '32e', 'dqwwddaSAd', NULL, '2022-11-07 15:09:38.97410', 1, NULL, NULL),
(11, 'YL Curse Title', 'Does this work?', 'google.com', NULL, '2022-11-16 15:34:49.717901', 1, NULL, NULL),
(14, 'saefwegv', '1', 'dsfvr', NULL, '2022-12-01 17:27:29.745754', 2, NULL, NULL),
(15, 'fgrvri', 'svdv', 'dbtbymj', NULL, '2022-12-01 17:27:29.745754', 2, NULL, NULL);

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
  `progress` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employee_course`
--

INSERT INTO `employee_course` (`employee_id`, `course_id`, `manager_id`, `answer`, `feedback`, `progress`) VALUES
(4, 14, 2, NULL, NULL, '0.00'),
(4, 15, 2, NULL, NULL, NULL),
(5, 14, 2, NULL, NULL, NULL),
(6, 14, 2, NULL, NULL, NULL),
(6, 15, 2, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `question`
--

CREATE TABLE `question` (
  `questionId` int(11) NOT NULL,
  `data` varchar(500) DEFAULT NULL,
  `maxPoints` int(11) DEFAULT NULL,
  `link` varchar(50) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `question`
--

INSERT INTO `question` (`questionId`, `data`, `maxPoints`, `link`, `course_id`) VALUES
(64, 'sefcesiij', 1, 'svrsrth', 14),
(65, 'wgrvftebt', 123, 'dfvbrb', 14),
(66, 'wegfrb', 34, 'fvrb', 14),
(67, '3rd question, what is the radius of the moon when a cow jumps over a cheese grater?', 100, NULL, 14),
(69, 'REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY', 20, NULL, 14),
(74, 'REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG ', 100, NULL, 14),
(75, 'REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG REALLY LONG ', 100, NULL, 14),
(76, 'new question', 42, NULL, 15),
(77, 'A very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very long question', 100, NULL, 15);

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
  `manager_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `firstname`, `lastname`, `email`, `isManager`, `isSupManager`, `password`, `manager_id`) VALUES
(1, 'Yan', 'Li', 'YAN.LI@wdc.com', 'Y', 'Y', '1234', NULL),
(2, 'Shirley', 'Liu', 'Shirleu.Liu@wdc.com', 'Y', 'Y', '1234', 1),
(3, 'Mike', 'Langberg', 'Mike.Langberg@wdc.com', 'Y', 'N', '1234', 1),
(4, 'Ashmir', 'Moni', 'amoni@wdc.com', 'N', 'N', '1234', 2),
(5, 'Wilfred', 'Yomba', 'wngongyomba@wdc.com', 'N', 'N', '1234', 2),
(6, 'Gursagar', 'Singh', 'gsingh96@wdc.com', 'N', 'N', '1234', 2),
(7, 'Socheata', 'Hour', 'shour@wdc.com', 'N', 'N', '1234', 3),
(8, 'Sarah', 'Padilla', 'spadilla27@wdc.com', 'N', 'N', '1234', 3),
(9, 'Justin', 'Dumindin', 'jdumindin@wdc.com', 'N', 'N', '1234', 3);

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
  MODIFY `idcourses` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `question`
--
ALTER TABLE `question`
  MODIFY `questionId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=78;

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
