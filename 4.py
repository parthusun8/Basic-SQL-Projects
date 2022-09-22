import sqlite3

conn = sqlite3.connect("q4.db")
conn.execute("CREATE TABLE IF NOT EXISTS MOVIES (Movie_ID INT(4), Movie_Name varchar(400), Genre varchar(20), Language TEXT, Rating FLOAT);")

conn.commit()

conn.execute("INSERT INTO MOVIES VALUES (101, 'Dark', 'SCI-FI', 'GERMAN', '4.6')")
conn.execute("INSERT INTO MOVIES VALUES (102, 'Doctor Strange', 'SCI-FI', 'ENGLISH', '4.3')")
conn.execute("INSERT INTO MOVIES VALUES (103, 'Bhuj Jod', 'DOCUMENTARY', 'HINDI', '3.6')")
conn.execute("INSERT INTO MOVIES VALUES (104, 'Karate Kid', 'ACTION', 'JAPANESE', '2.6')")
conn.execute("INSERT INTO MOVIES VALUES (105, 'TE3N', 'FICTION', 'MARATHI', '1.8')")

conn.commit()

print("2A : ")
conn.execute("UPDATE MOVIES SET Rating=Rating + 0.1")
conn.commit()

print("Total Rows affected ", conn.total_changes)
res = conn.execute("SELECT * FROM MOVIES")
for row in res:
    print("Movie_id : ", row[0])
    print("Movie Name : ", row[1])
    print("Genre : ", row[2])
    print("Language : ", row[3])
    print("Rating : ", row[4])
    print("\n")

print("2B : ")
res = conn.execute("DELETE FROM MOVIES WHERE Movie_ID = 102")
print("Total Rows affected ", conn.total_changes)

print("2C : ")
res = conn.execute("SELECT * FROM MOVIES WHERE Rating > 3")
for row in res:
    print("Movie_id : ", row[0])
    print("Movie Name : ", row[1])
    print("Genre : ", row[2])
    print("Language : ", row[3])
    print("Rating : ", row[4])
    print("\n")

conn.close()

















