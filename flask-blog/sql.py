#sql.py  - Create a SQLite3 table and populate it with data

import sqlite3

#create a new database id the db does;nt aleady exist.
with sqlite3.connect("blog.db") as connection:
	#get a cursor object to execute SQL commands
	cur = connection.cursor()

	#create the table
	cur.execute("""CREATE TABLE posts
				(title TEXT, post TEXT)
				""")

	#insert dummy data into the table
	cur.execute('INSERT INTO posts VALUES("GOOD", "I\'m good")')
	cur.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
	cur.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent")')

