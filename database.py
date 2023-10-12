import sqlite3
from datetime import datetime as dt
import math

conn = sqlite3.connect('classrom_data.db')
cur = conn.cursor()
cur.execute("PRAGMA foreign_keys = ON")


cur.execute('''
    CREATE TABLE IF NOT EXISTS classrooms (
    id integer PRIMARY KEY AUTOINCREMENT,
    name text, 
    teacher text,
    class_size integer
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS data (
    temperature integer,
    humidity integer,
    distance_changed integer,
    audio integer,
    recorded_time integer,
    class_id integer,
    FOREIGN KEY (class_id) REFERENCES classrooms(id)
    )
''')
# distance_changed - √((x1-x2)^2+(y1-y2)^2+(z1-z2)^2), using accelerometer values x,y,z
conn.commit()

# # Insert test data into classrooms table
# cur.execute("INSERT INTO classrooms (name, teacher, class_size) VALUES (?, ?, ?)", ("Math", "Mr. Smith", 101))
# cur.execute("INSERT INTO classrooms (name, teacher, class_size) VALUES (?, ?, ?)", ("Science", "Ms. Johnson", 202))
# cur.execute("INSERT INTO classrooms (name, teacher, class_size) VALUES (?, ?, ?)", ("History", "Mr. Brown", 303))

# # Insert test data into data table
# cur.execute("INSERT INTO data (temperature, humidity, distance_changed, audio, recorded_time, class_id) VALUES (?, ?, ?, ?, ?, ?)", (72, 50, 10, 1, 1630543200, 1))
# cur.execute("INSERT INTO data (temperature, humidity, distance_changed, audio, recorded_time, class_id) VALUES (?, ?, ?, ?, ?, ?)", (68, 45, 15, 0, 1630543260, 1))
# cur.execute("INSERT INTO data (temperature, humidity, distance_changed, audio, recorded_time, class_id) VALUES (?, ?, ?, ?, ?, ?)", (75, 55, 5, 1, 1630543320, 2))
# cur.execute("INSERT INTO data (temperature, humidity, distance_changed, audio, recorded_time, class_id) VALUES (?, ?, ?, ?, ?, ?)", (70, 50, 20, 0, 1630543380, 2))
# cur.execute("INSERT INTO data (temperature, humidity, distance_changed, audio, recorded_time, class_id) VALUES (?, ?, ?, ?, ?, ?)", (68, 45, 10, 1, 1630543440, 3))
# cur.execute("INSERT INTO data (temperature, humidity, distance_changed, audio, recorded_time, class_id) VALUES (?, ?, ?, ?, ?, ?)", (72, 50, 5, 0, 1630543500, 3))

# # Commit changes to the database
# conn.commit()

'''query = cur.execute("SELECT * FROM classrooms")

query = query.fetchall()
for row in query:
    print(row)

query = cur.execute("SELECT * FROM data")

query = query.fetchall()
for row in query:
    print(row)'''

#print(dt.strftime(dt.now(), "%Y-%m-%d %H:%M:%S"))

# function to insert data into data table

def distance_changed(x, y, z):
    return math.sqrt((x)^2+(y)^2+(z)^2)

def insert_data(temperature, humidity, x, y, z, audio, class_id):
    cur.execute("INSERT INTO data (temperature, humidity, distance_changed, audio, recorded_time, class_id) VALUES (?, ?, ?, ?, ?, ?)", (temperature, humidity, distance_changed(x, y, z), audio, dt.now(), class_id))
    conn.commit()