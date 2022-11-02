-- CREATE SCHEMA userdb;
-- drop table user;
-- drop DATABASE userdb;
CREATE TABLE `user` (
  `id` int(20) NOT NULL auto_increment,
  `firstname` varchar(50)  NULL,
  `lastname` varchar(30)  NULL,
  `email` varchar(40) DEFAULT NULL,
  `employeeID` char(12) DEFAULT NULL,
  `isManager` char(1) NOT NULL,
  `isSupManager` char(1) NOT NULL,
  `password` varchar(40) NOT NULL,
  Constraint pk_idcustomer Primary key (id)
) ;
insert into user
(firstname,lastname,email,employeeID,isManager,isSupManager,password)



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

Create TABLE `userdb`.`courses` (
  `idcourses` int(20) NOT NULL auto_increment,
  `courseTitle` varchar(25)  NULL,
  `courseQues` varchar(150)  NULL,
  `courseLink` varchar(50) DEFAULT NULL,
  `courseFeedback` varchar(150) DEFAULT NULL,
  `courseCreatTime` varchar(25) NOT NULL,
  `courseStart` varchar(25) NOT NULL,
  `courseEnd` varchar(25) NOT NULL,
  `user_id` int PRIMARY KEY, FOREIGN KEY (user_id) REFERENCES user(id));

INSERT INTO `userdb`.`courses`
(idcourses,
courseTitle,
courseQues,
courseLink,
courseFeedback,
courseTime
)
VALUES
('1','course1',
'What is the first question',
'www.google.com',
'This is the manager feedback',
NOW());
-- drop table `userdb`.`courses`

