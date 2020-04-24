import sqlite3
conn = sqlite3.connect('tabletop.db')
c = conn.cursor()
def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS students(id INT PRIMARY KEY NOT NULL, last_name TEXT(50) NOT NULL, first_name TEXT(50) NOT NULL, email TEXT(50), discord_id TEXT(50))')
create_table()
