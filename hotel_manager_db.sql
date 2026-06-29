-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 11, 2024 at 09:37 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel_manager_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking_table`
--

CREATE TABLE `booking_table` (
  `Reg_No` int(10) NOT NULL,
  `Name` varchar(200) NOT NULL,
  `Phone` bigint(30) NOT NULL,
  `UID` bigint(30) NOT NULL,
  `Check_In` date NOT NULL,
  `Check_Out` date NOT NULL,
  `Total_guests` int(30) NOT NULL,
  `payment_status` varchar(100) NOT NULL,
  `mode` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking_table`
--

INSERT INTO `booking_table` (`Reg_No`, `Name`, `Phone`, `UID`, `Check_In`, `Check_Out`, `Total_guests`, `payment_status`, `mode`) VALUES
(1, 'aman', 9879879877, 789798783, '2023-03-30', '2023-04-20', 5, 'Pending', 'Cash');

-- --------------------------------------------------------

--
-- Table structure for table `roominfo_table`
--

CREATE TABLE `roominfo_table` (
  `Reg_No` int(10) NOT NULL,
  `Room_Type` varchar(100) NOT NULL,
  `Room_no` varchar(100) NOT NULL,
  `room_bed_type` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `floor` varchar(100) NOT NULL,
  `room_price` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roominfo_table`
--

INSERT INTO `roominfo_table` (`Reg_No`, `Room_Type`, `Room_no`, `room_bed_type`, `status`, `floor`, `room_price`) VALUES
(2, 'Non-AC with meal', '102', 'Double Bed', 'Non-Available', '2', 3300);

-- --------------------------------------------------------

--
-- Table structure for table `usertable`
--

CREATE TABLE `usertable` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `usertype` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `usertable`
--

INSERT INTO `usertable` (`username`, `password`, `usertype`) VALUES
('jyoti', '123', 'Admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking_table`
--
ALTER TABLE `booking_table`
  ADD PRIMARY KEY (`Reg_No`);

--
-- Indexes for table `roominfo_table`
--
ALTER TABLE `roominfo_table`
  ADD PRIMARY KEY (`Room_no`) USING BTREE;

--
-- Indexes for table `usertable`
--
ALTER TABLE `usertable`
  ADD PRIMARY KEY (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
