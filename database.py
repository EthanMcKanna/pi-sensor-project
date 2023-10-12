#import os
import sqlite3

conn = sqlite3.connect('classrom_data.db')
cur = conn.cursor()
cur.execute("PRAGMA foreign_keys = ON")


cur.execute('''
    CREATE TABLE IF NOT EXISTS classrooms (
    id integer PRIMARY KEY AUTOINCREMENT,
    name text, 
    teacher text,
    class integer
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS data (
    temperature integer,
    humidity integer,
    accelerometer_x integer,
    accelerometer_y integer,
    accelerometer_z integer,
    audio integer,
    recorded_time integer,
    class_id integer,
    FOREIGN KEY (class_id) REFERENCES classrooms(id)
    )
''')
