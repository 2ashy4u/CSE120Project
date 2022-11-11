-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 11, 2022 at 05:50 AM
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
-- Database: `users`
--

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `idcourses` int(11) NOT NULL,
  `courseTitle` varchar(25) DEFAULT NULL,
  `courseQues` varchar(150) DEFAULT NULL,
  `courseLink` varchar(50) DEFAULT NULL,
  `courseFeedback` varchar(150) DEFAULT NULL,
  `courseTime` varchar(30) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`idcourses`, `courseTitle`, `courseQues`, `courseLink`, `courseFeedback`, `courseTime`, `user_id`) VALUES
(5, NULL, 'Is this a course?', NULL, NULL, 'now', 1),
(6, NULL, 'hahahaha', NULL, NULL, 'now', 1),
(7, 'asDqwd', '32e', 'dqwwddaSAd', NULL, '2022-11-07 15:09:38.97410', 1);

-- --------------------------------------------------------

--
-- Table structure for table `employee_course`
--

CREATE TABLE `employee_course` (
  `employee_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `manager_id` int(11) NOT NULL,
  `answer` varchar(150) DEFAULT NULL,
  `feedback` varchar(150) DEFAULT NULL
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
(8, 'Sarah', 'Padilla', 'spadilla27@@wdc.com', 'N', 'N', '1234', 3),
(9, 'Justin', 'Dumindin', 'jdumindin@wdc.com', 'N', 'N', '1234', 3);

--
-- Indexes for dumped tables
--

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
  ADD PRIMARY KEY (`employee_id`,`course_id`,`manager_id`),
  ADD KEY `course_id` (`course_id`),
  ADD KEY `manager_id` (`manager_id`);

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
  MODIFY `idcourses` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Constraints for dumped tables
--

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
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`manager_id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
