import sqlite3
from datetime import datetime as dt
import math

conn = sqlite3.connect('classrom_data.db')
cur = conn.cursor()
cur.execute("PRAGMA foreign_keys = ON")



cur.execute('''
    CREATE TABLE IF NOT EXISTS data (
    teacher text,
    block text,
    class_size integer,
    temperature integer,
    humidity integer,
    distance_changed integer,
    audio integer,
    recorded_time integer
    )
''')
# distance_changed - √((x1-x2)^2+(y1-y2)^2+(z1-z2)^2), using accelerometer values x,y,z
conn.commit()

# Insert test data into data table
cur.execute("INSERT INTO data (teacher, block, class_size, temperature, humidity, distance_changed, audio, recorded_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", ('moneyhon', 'G', 13, 72, 50, 10, 1, 1630543200))
cur.execute("INSERT INTO data (teacher, block, class_size, temperature, humidity, distance_changed, audio, recorded_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", ('dixon', 'A', 16, 68, 45, 15, 0, 1630543260))
cur.execute("INSERT INTO data (teacher, block, class_size, temperature, humidity, distance_changed, audio, recorded_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", ('eaton', 'D', 17, 75, 55, 5, 1, 1630543320))
cur.execute("INSERT INTO data (teacher, block, class_size, temperature, humidity, distance_changed, audio, recorded_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", ('pruitt', 'A', 14, 70, 50, 20, 0, 1630543380))
cur.execute("INSERT INTO data (teacher, block, class_size, temperature, humidity, distance_changed, audio, recorded_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", ('schinetsky', 'E', 9, 68, 45, 10, 1, 1630543440))

# # Commit changes to the database
# conn.commit()

query = cur.execute("SELECT * FROM data")

query = query.fetchall()
for row in query:
    print(row)


#print(dt.strftime(dt.now(), "%Y-%m-%d %H:%M:%S"))

# function to insert data into data table

def distance_changed(x, y, z):
    return math.sqrt((x)^2+(y)^2+(z)^2)
'''
def insert_data(temperature, humidity, x, y, z, audio, class_id):
    cur.execute("INSERT INTO data (temperature, humidity, distance_changed, audio, recorded_time, class_id) VALUES (?, ?, ?, ?, ?, ?)", (temperature, humidity, distance_changed(x, y, z), audio, dt.now(), class_id))
    conn.commit()'''