import sqlite3

conn = sqlite3.connect("q3.db")
print("Database opened Successfully ")

conn.execute("CREATE TABLE IF NOT EXISTS RECIPES ("
             "ID INT(11), NAME varchar(400), DESCRIPTION TEXT, CATEGORY_ID INT, CHEF_ID varchar(5), "
             "CREATED DATETIME);")
conn.commit()

conn.execute("INSERT INTO RECIPES VALUES (1, 'Butter Chicken', 'Indian', 2563, 'A201', '21.04.2002')")
conn.execute("INSERT INTO RECIPES VALUES (2, 'Butter Corn', 'Mexican', 4586, 'A201', '25.08.2003')")
conn.execute("INSERT INTO RECIPES VALUES (3, 'Pasta', 'Italian', 9656, 'C208', '21.04.2004')")
conn.execute("INSERT INTO RECIPES VALUES (4, 'Noodles', 'Chinese', 5632, 'E204', '21.04.2005')")
conn.execute("INSERT INTO RECIPES VALUES (5, 'Momos', 'Chinese', 1863, 'D207', '21.04.2006')")
conn.commit()

res = conn.execute("SELECT * FROM RECIPES WHERE DESCRIPTION = 'Chinese'")
for row in res:
    print("Name : ", row[1])
    print("Description : ", row[2])
    print("Created : ", row[5])
    print("\n")

res = conn.execute("SELECT ID, NAME FROM RECIPES WHERE CHEF_ID = 'A201'")
for row in res:
    print("ID : ", row[0])
    print("NAME : ", row[1])
    print("\n")

res = conn.execute("SELECT DESCRIPTION FROM RECIPES WHERE NAME LIKE 'P%'")
for row in res:
    print("DESCRIPTION : ", row[0])
    print("\n")

print("ALL CHANGES DONE")
conn.close()

