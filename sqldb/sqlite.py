import sqlite3

conn = sqlite3.connect('school.db')

cursor = conn.cursor()
# cursor.execute('''
#        CREATE TABLE students (
#               id INTEGER PRIMARY KEY AUTOINCREMENT,
#               name TEXT NOT NULL,
#               age INTEGER,
#               course TEXT NOT NULL 
#        )
# ''')

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
cursor.execute('''
     INSERT INTO students  (name,age,course) VALUES (?,?,?)
''',('Athul',20,'cs'))
cursor = 'cs'
id = 6
cursor.execute('''
     UPDATE students
     SET course = ?
     WHERE id =?
''',(course,id))

cursor.execute('''
     DELETE 
     FROM students
     WHERE id =?
''',(4,))
conn.commit()

cursor.execute('''
    SELECT *
    FROM students
''')
cursor.execute('''
    SELECT name
    FROM students
''')
cursor.execute('''
    SELECT name, course
    FROM students
''')
cursor.execute('''
    SELECT *
    FROM students
    WHERE course =?
''',('cs'))
cursor.execute('''
    SELECT *
    FROM students
    WHERE age > ? AND name LIKE ?
''',(19,'A%'))
cursor.execute('''
    SELECT *
    FROM students
    WHERE age > ? AND name LIKE ?
''',(19,'%1'))
cursor.execute('''
    SELECT *
    FROM students
    WHERE age > ? AND name LIKE ?
''',(19,'%n%'))

cursor.execute('''
    SELECT COUNT (*)
    FROM students
    WHERE age > ?
''',(21,))

data = cursor.fetchall()
data = cursor.fetchmany(5)
data = cursor.fetchone()
print(data)
cursor.execute('''
    SELECT SUM (age)
    FROM students
''')
print(cursor.fetchone())
cursor.execute('''
    SELECT AVG(age)
    FROM students
''')
print(cursor.fetchone())

cursor.execute('''
    SELECT MIN(age)
    FROM students
''')
print(cursor.fetchone())

cursor.execute('''
    SELECT MAX(age)
    FROM students
''')
print(cursor.fetchone())
cursor.execute('ALTER TABLE students ADD COLUMN register_no INTEGER')
cursor.execute('ALTER TABLE students RENAME COLUMN course TO department')
cursor.execute('ALTER TABLE synnefo RENAME TO students')
cursor.execute('DROP TABLE IF EXISTS students')
cursor.execute('''
    SELECT *'
    FROM students
    ORDER BY name DESC
''')
print(cursor.fetchall())
conn.close()
