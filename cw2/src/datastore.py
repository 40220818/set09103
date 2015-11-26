from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask(__name__)

db_location = 'var/sqlite3.db'

def get_db():
	db = getattr (g, 'db', None)
	if db is None:
		db = sqlite3.connect(db_location)
		g.db = db
	return db

@app.teardown_appcontext
def close_db_connection(exception):
	db = getattr(g, 'db', None)
	if db is not None:
		db.close()

def init_db():
	with app.app_context():
		db = get_db()
		with app.open_resource('schema.sql', mode ='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

def addUser(name, user, email, pw):
	db = get_db()
	db.cursor().execute('INSERT INTO users VALUES (?, ?, ?, ?)', (name, user, email, pw))
	db.commit()
	
def getUserPassword(user):
	db = get_db()
	result = db.cursor().execute('SELECT pass FROM users WHERE user=?', (user,)).fetchone()
	if result is not None:
		return result[0] #the password is the 0 position because in the select we only put the pass column
	return None
	
def getUser(user):
	db = get_db()
	result = db.cursor().execute('SELECT * FROM users WHERE user=?', (user,)).fetchone()
	return result
	
def searchUser(key):
	db = get_db()
	likeKey = '%'+key+'%'
	results = db.cursor().execute('SELECT * FROM users WHERE user LIKE ? OR name LIKE ?', (likeKey,likeKey,)).fetchall()
	return results
	
def addImage(user, image, desc, date):
	#with open(image, 'rb') as input_file:
	ablob = image.read()
	#ablob = image.file.read()
	db = get_db()
	db.cursor().execute('INSERT INTO images VALUES (?, ?, ?, ?)', (user, sqlite3.Binary(ablob), desc, date))
	db.commit()
		
def getImages(user):
	db = get_db()
	results = db.cursor().execute('SELECT * FROM images WHERE user=? ORDER BY date DESC', (user,)).fetchall()
	return results