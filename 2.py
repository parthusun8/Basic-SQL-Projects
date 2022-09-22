"""2. Create a table for Student with the following fields (Reg_no,stud_name,sex, and create a
table Dept with the following fields(dept_no primary key, dept_name)
a. Insert sample records and do the following
b. Display the student reg_no,name and dept_name
c. Display the student names ending with „ka‟
d. Display all the female students name
e. Display the student names by descending order"""

import sqlite3

conn = sqlite3.connect("q2.db")
print("Opened Database Successfully")
conn.execute(
    "CREATE TABLE IF NOT EXISTS STUDENTS (ID INT PRIMARY KEY NOT NULL, Reg_no TEXT NOT NULL, Stud_name TEXT NOT NULL, sex CHAR NOT NULL);")
conn.commit()
conn.execute("CREATE TABLE IF NOT EXISTS DEPT (Dept_no INT PRIMARY KEY NOT NULL, dept_name TEXT NOT NULL);")
conn.commit()
conn.execute("INSERT INTO STUDENTS VALUES(1, 'RA2011029010051', 'Parth Sundarka', 'M')")
conn.execute("INSERT INTO STUDENTS VALUES(2, 'RA2011029010034', 'Rishi Pratap', 'M')")
conn.execute("INSERT INTO STUDENTS VALUES(3, 'RA2011029010032', 'Abhijit Prajapati', 'F')")
conn.execute("INSERT INTO STUDENTS VALUES(4, 'RA2011029010020', 'Aditya Pathak', 'M')")
conn.execute("INSERT INTO STUDENTS VALUES(5, 'RA2011029010022', 'Harshit Prakash', 'O')")
conn.commit()
conn.execute("INSERT INTO DEPT VALUES(1, 'CSE')")
conn.execute("INSERT INTO DEPT VALUES(2, 'ECE')")
conn.execute("INSERT INTO DEPT VALUES(3, 'EEE')")
conn.execute("INSERT INTO DEPT VALUES(4, 'ELECTRICAL')")
conn.execute("INSERT INTO DEPT VALUES(5, 'MECHANICAL')")
conn.commit()


print("2B :")
res = conn.execute("SELECT Reg_no, Stud_name, dept_name FROM STUDENTS, DEPT WHERE DEPT.Dept_no = STUDENTS.ID")
for row in res:
    print("Regd_no : ", row[0])
    print("Student Name : ", row[1])
    print("Department : ", row[2])
    print("\n")


print("2C :")
res = conn.execute("SELECT * FROM STUDENTS where Stud_name like '%ka'")
for row in res:
    print("Regd_no : ", row[1])
    print("Student Name : ", row[2])
    print("Sex : ", row[3])
    print("\n")

print("2D : ")
res = conn.execute("SELECT * from STUDENTS where sex = 'M'")
for row in res:
    print("Regd_no : ", row[1])
    print("Student Name : ", row[2])
    print("Sex : ", row[3])
    print("\n")

print("2E : ")
res = conn.execute("SELECT * FROM STUDENTS ORDER by Stud_name DESC")
for row in res:
    print("Regd_no : ", row[1])
    print("Student Name : ", row[2])
    print("Sex : ", row[3])
    print("\n")


conn.close()
