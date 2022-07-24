        import mysql.connector

        """ Connect to MySQL database """

        conn = mysql.connector.connect(host='localhost',
                                       database = 'students',
                                       user = 'root',
                                       password = 'Sakshi500604')

        if conn.is_connected():
            print('Connected to MySOL database')

        # Creating a cursor object using the cursor()
        cursor = conn.cursor()

        # Executing an MySQL function using the execute() method
        sql = "SELECT * FROM students.`students_details`"

        #Executing the query
        cursor.execute(sql)

        #Fetching 1st row from the table
        result = cursor.fetchall()
        print(result)


        # ii. Take input from the user and add it to the database
        prn = int(input("Enter PRN: "))
        fname = input("First name: ")
        mname = input("Middle name: ")
        lname = input("Last name: ")
        addr = input("Address: ")
        mob = input("Mobile no. ")
        email = input("E-mail: ")
        age = int(input("Age: "))
        sql = "INSERT INTO students.students_details VALUES (prn,fname,mname,lname,addr,mob,email,age)"
        cursor.execute(sql)
        conn.commit()
        print(cursor.rowcount, "record inserted.")


        # iii. Delete a user by taking the PRN number as input
        sql = "DELETE FROM students.students_details WHERE PRN = 5010"
        cursor.execute(sql)
        conn.commit()
        print(cursor.rowcount, "record deleted")

        # iv. Update user details (Phone number and email id.)
        sql = "UPDATE students.students_details SET `Mobile no.` = '8954673289', `E-mail`='sakshijadhav046@gmai.com' WHERE PRN = 5043"
        cursor.execute(sql)
        conn.commit()
        print(cursor.rowcount, "record updated")

        # v. Add a new column “CGPA” to the table and enter CGPA for all students.
        query_1 = "ALTER TABLE students.students_details ADD CGPA float(20)"
        query_2 = "UPDATE students.students_details SET `CGPA` = '8.35' where PRN=5010"
        query_3 = "UPDATE students.students_details SET `CGPA` = '8.27' where PRN=5015"
        query_4 = "UPDATE students.students_details SET `CGPA` = '9.47' where PRN=5031"
        query_5 = "UPDATE students.students_details SET `CGPA` = '7.18' where PRN=5042"
        query_6 = "UPDATE students.students_details SET `CGPA` = '8.77' where PRN=5043"

        cursor.execute(query_1)
        cursor.execute(query_2)
        cursor.execute(query_3)
        cursor.execute(query_4)
        cursor.execute(query_5)
        cursor.execute(query_6)
        conn.commit()

        print(cursor.rowcount, "record(s) updated")

        # vi. Display the final table.
        cursor.execute("select * from students.students_details")
        myresult = cursor.fetchall()
        for row in myresult:
            print(row)

        # Closing the connection
        conn.close()


