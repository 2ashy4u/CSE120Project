# CSE120Project
Training App Capstone Project

By default the SQL_ALCHEMY_URI is set to root:@127.0.0.1:3306
Code requires the "users" database to use:

CREATE DATABASE users;
-- drop table user;
-- drop DATABASE users;

CREATE TABLE `user` (
  `id` int(20) NOT NULL auto_increment,       -- 'idcustomer' changed to 'id'
  `firstname` varchar(50)  NULL,
  `lastname` varchar(30)  NULL,
  `email` varchar(40) DEFAULT NULL,
  `employeeID` char(12) DEFAULT NULL,
  `isManager` char(1) NOT NULL,
  `isSupManager` char(1) NOT NULL,
  `password` varchar(40) NOT NULL,            -- 'pass' changed to 'password'
  Constraint pk_idcustomer Primary key (id)   -- 'idcustomer' changed to 'id'
) ;

insert into user
(firstname,lastname,email,employeeID,isManager,isSupManager,password)   -- 'pass' changed to 'password'
-- Super Managers
values
('Yan','Li','YAN.LI@wdc.com','1','Y','Y',1234), 
('Shirley','Liu','Shirleu.Liu@wdc.com','2','Y','Y',1234),
-- Managers 
('Mike','Langberg','Mike.Langberg@wdc.com','3','Y','N',1234), 
-- Employees
('Ashmir','Moni','amoni@wdc.com','4','N','N',1234),
('Wilfred','Yomba','wngongyomba@wdc.com','5','N','N',1234), 
('Gursagar','Singh','gsingh96@wdc.com','6','N','N',1234), 
('Socheata','Hour','shour@wdc.com','7','N','N',1234), 
('Sarah','Padilla','spadilla27@@wdc.com','8','N','N',1234),
('Justin','Dumindin','jdumindin@wdc.com','9','N','N',1234);     
select * from user
