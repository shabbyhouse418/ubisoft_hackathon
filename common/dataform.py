import random
import sqlite3


conn = sqlite3.connect('./DB/data')
c = conn.cursor()

try:
    c.execute('''CREATE TABLE INI_TABLE(
        ID          INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        CLASS1      INT                     NOT NULL,
        CLASS2      INT                     NOT NULL,
        CLASS3      INT                     NOT NULL,
        CLASS4      INT                     NOT NULL,
        CLASS5      INT                     NOT NULL,
        CLASS6      INT                     NOT NULL,
        CLASS7      INT                     NOT NULL,
        CLASS8      INT                     NOT NULL); ''')

except sqlite3.OperationalError as OperationalError:
    print("sqlite3.OperationalError",end="")
    print(OperationalError)
finally:
    conn.commit()
    conn.close()
'''
for i in range(2000):
    MAXLENGTH = 12
    class1 = random.randint(0,MAXLENGTH)
    class2 = random.randint(0,MAXLENGTH - class1)
    class3 = random.randint(0,MAXLENGTH - class1 - class2)
    class4 = MAXLENGTH - class1 - class2 - class3

    class5 = random.randint(0,MAXLENGTH)
    class6 = random.randint(0,MAXLENGTH - class5)
    class7 = random.randint(0,MAXLENGTH - class5 - class6)
    class8 = MAXLENGTH - class5 - class6 - class7

    conn = sqlite3.connect('./DB/data')
    c = conn.cursor()

    c.execute("INSERT INTO class (CLASS1, CLASS2, CLASS3, CLASS4, CLASS5, CLASS6, CLASS7, CLASS8) \
      VALUES (%d, %d, %d, %d, %d, %d, %d, %d)"%(class1, class2, class3, class4, class5, class6, class7, class8))
    
    conn.commit()

for i in range(500):
    class1 = random.randint(0,MAXLENGTH)
    class2 = random.randint(0,MAXLENGTH - class1)
    class3 = random.randint(0,MAXLENGTH - class1 - class2)
    class4 = MAXLENGTH - class1 - class2 - class3
    c.execute("INSERT INTO class (CLASS1, CLASS2, CLASS3, CLASS4, CLASS5, CLASS6, CLASS7, CLASS8) \
      VALUES (%d, %d, %d, %d, %d, %d, %d, %d)"%(class1, class2, class3, class4, class1, class2, class3, class4))
    conn.commit()

cursor = c.execute("SELECT * from class")

for row in cursor:
    print("ID = ", row[0])
    print("CLASS1 = ", row[1])
    print("CLASS2 = ", row[2])
    print("CLASS3 = ", row[3])
    print("CLASS4 = ", row[4])
    print("CLASS5 = ", row[5])
    print("CLASS6 = ", row[6])
    print("CLASS7 = ", row[7])
    print("CLASS8 = ", row[8])
'''
conn.close()