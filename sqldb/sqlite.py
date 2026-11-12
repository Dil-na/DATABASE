import sqlite3

conn = sqlite3.connect('school.db')

cursor = conn.cursor()
cursor.execute('''
       CREATE TABLE students(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL,
       age INTEGER,
       course TEXT NOT NULL
       )
''')

cursor.execute('''
       INSERT INTO students (name,age,course) VALUES (?,?,?)

''',('Anu',22,'civil'))
conn.commit()

cursor.execute('''
       INSERT INTO students (name,age,course) VALUES (?,?,?)

''',('Ammu',22,'cs'))
conn.commit()
cursor.execute('''
       INSERT INTO students (name,age,course) VALUES (?,?,?)

''',('Abi',20,'ECE'))
conn.commit()
cursor.execute('''
       INSERT INTO students (name,age,course) VALUES (?,?,?)

''',('malu',21,'eee'))
conn.commit()
cursor.execute('''
       INSERT INTO students (name,age,course) VALUES (?,?,?)

''',('dilna',22,'cs'))
conn.commit()
cursor.execute('''
       INSERT INTO students (name,age,course) VALUES (?,?,?)

''',('viky',23,'python'))
conn.commit()
cursor.execute('''
       INSERT INTO students (name,age,course) VALUES (?,?,?)

''',('amal',24,'civil'))
conn.commit()
cursor.execute('''
       INSERT INTO students (name,age,course) VALUES (?,?,?)

''',('Ashin',23,'ece'))
conn.commit()
cursor.execute('''
       INSERT INTO students (name,age,course) VALUES (?,?,?)

''',('arun',25,'chemical'))
conn.commit()
cursor.execute('''
       INSERT INTO students (name,age,course) VALUES (?,?,?)

''',('rithin',26,'Digital marketing'))
conn.commit()


cursor.execute('''
    SELECT *
    FROM students
''')

data = cursor.fetchall()
print(data)
conn.close()