CREATE TABLE `students_details` (
  `PRN` int NOT NULL,
  `First name` varchar(15) NOT NULL,
  `Middle name` varchar(15) NOT NULL,
  `Last name` varchar(15) NOT NULL,
  `Address` varchar(45) NOT NULL,
  `Mobile no.` varchar(12) NOT NULL,
  `E-mail` varchar(25) NOT NULL,
  `Age` int NOT NULL,
  PRIMARY KEY (`PRN`)
)
SELECT * FROM students.students_details;