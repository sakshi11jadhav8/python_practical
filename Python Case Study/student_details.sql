CREATE TABLE `students_details` (
  `PRN` int NOT NULL,
  `First name` varchar(45) NOT NULL,
  `Middle name` varchar(45) NOT NULL,
  `Last name` varchar(45) NOT NULL,
  `Address` varchar(45) NOT NULL,
  `Mobile no.` varchar(45) NOT NULL,
  `E-mail` varchar(45) NOT NULL,
  `Age` int NOT NULL,
  PRIMARY KEY (`PRN`)
)
SELECT * FROM students.students_details;
