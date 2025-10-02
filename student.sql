-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 26, 2025 at 03:13 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student`
--

-- --------------------------------------------------------

--
-- Table structure for table `student_data`
--

CREATE TABLE `student_data` (
  `id` varchar(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `phone` int(200) NOT NULL,
  `gender` varchar(200) NOT NULL,
  `course` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student_data`
--

INSERT INTO `student_data` (`id`, `name`, `phone`, `gender`, `course`) VALUES
('0025', 'Jonas D. Guadalupe', 855952, 'Male', 'BSCRIM'),
('002566', 'Sheila Faith Talledo', 78995, 'Female', 'BSED'),
('003-26', 'Jeggy Boy', 8080, 'Female', 'BSCRIM'),
('0078-25', 'Maria Labo', 5454545, 'Female', 'BSCRIM'),
('10120', 'James De Guzman', 878978, 'Male', 'BSECE'),
('18564', 'John Martin Lhuther Jr', 80808787, 'Male', 'BSECE'),
('252-26', 'Mark Scukerburge', 84558, 'Male', 'BSCE'),
('456789', 'sharon', 864684, 'Male', 'BSHM'),
('4756', 'fghjkl', 456, 'Female', 'BSECE'),
('54864864', 'dfghjkl;', 456, 'Female', 'BSHM'),
('7', 'Rhea Dela Cruz', 78, 'Female', 'BSECE');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(200) NOT NULL,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`) VALUES
(1, 'admin', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student_data`
--
ALTER TABLE `student_data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
