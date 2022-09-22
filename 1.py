# CREATING THE TABLE
"""Write a SQL lites statement to create a table names as employees including columns
employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary,
commission, manager_id and department_id
i) Insert values in the table and also execute the table structure
ii) Display the first name, last name of an employees whose salary is greater than 25,000"""
import sqlite3

conn = sqlite3.connect('q1.db')
print("Opened database successfully")

conn.execute('''
CREATE TABLE IF NOT EXISTS EMPLOYEE
         (employee_id INT PRIMARY KEY NOT NULL,
         first_name TEXT NOT NULL,
         last_name TEXT NOT NULL,
         email TEXT NOT NULL,
         phone_number INT NOT NULL,
         hire_date TEXT NOT NULL,
         job_id INT NOT NULL,
         SALARY REAL NOT NULL,
         commission REAL NOT NULL,
         manager_id TEXT,
         dept_id TEXT);''')
conn.commit()

conn.execute("INSERT INTO EMPLOYEE VALUES(1, 'Parth', 'Sundarka', 'ps2644@srmist.edu.in', 7998561528, '21.04.2022', 32, 25000, 5248, 'A201', 'ARTS')")
conn.execute("INSERT INTO EMPLOYEE VALUES(2, 'Aditya', 'Pathak', 'ap8695@srmist.edu.in', 8595691563, '22.04.2022', 15, 20000, 5001, 'A202', 'FILM')")
conn.execute("INSERT INTO EMPLOYEE VALUES(3, 'Mahek', 'Kamani', 'mk4869@srmist.edu.in', 8569512345, '23.04.2022', 85, 19000, 5260, 'B201', 'ELECTRICAL')")
conn.execute("INSERT INTO EMPLOYEE VALUES(4, 'Rishi', 'Pratap', 'rp1985@srmist.edu.in', 8596321425, '24.04.2022', 96, 27000, 5855, 'C201', 'MECH')")
conn.execute("INSERT INTO EMPLOYEE VALUES(5, 'Amit', 'Shah', 'as1963@srmist.edu.in', 2356894515, '25.04.2022', 12, 23000, 4256, 'B202', 'ML')")
conn.execute("INSERT INTO EMPLOYEE VALUES(6, 'Narendra', 'Modi', 'nm5648@srmist.edu.in', 8659321526, '26.04.2022', 36, 52000, 8945, 'F204', 'AI')")
conn.commit()

data = conn.execute("SELECT first_name, last_name FROM EMPLOYEE WHERE salary > 25000")

for row in data:
    print("First Name : ", row[0])
    print("Last Name : ", row[1])


print("Table created successfully")

conn.close()
