import ConfigParser
import bcrypt
import logging

from datastore import addUser, getUserPassword
from logging.handlers import RotatingFileHandler
from functools import wraps
from flask import Flask, redirect, render_template, request, session, flash, url_for

app = Flask(__name__)
app.secret_key ='\xd1\xdb?\xe7!Y\xa5\xb8\xf0x\x17\xa8:\xa6\xfd\xf0\xdaH\x1b\xbe\xad\x11\x95|'

#valid_user = 'rubenyes@gmail.com'
#valid_pwhash = bcrypt.hashpw('secretpass', bcrypt.gensalt())

def check_auth(user, password):
	#if(user == valid_user and valid_pwhash == bcrypt.hashpw(password.encode('utf-8'), valid_pwhash)):
	pwhashStored = getUserPassword(user)
	print pwhashStored
	if(pwhashStored is not None and pwhashStored == bcrypt.hashpw(password.encode('utf-8'), pwhashStored)):
		return True
	return False

def requires_login(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		status = session.get('logged_in', False)
		if not status:
			return redirect(url_for('.root'))
		return f(*args, **kwargs)
	return decorated

@app.route('/logout/')
def logout():
	session['logged_in'] = False
	app.logger.info("User: "+user+" has log out.")
	return redirect(url_for('.root'))

@app.route("/secret/")
@requires_login
def secret():
	return "Secret Page"

@app.route("/login/", methods=['GET','POST'])
def login():
	if request.method =='POST':
		user = request.form['user']
		pw = request.form['password']
		if check_auth(user, pw):
			session['logged_in'] = True
			app.logger.info("User: "+user+" log in SUCCESFUL.")
			return redirect(url_for('.secret'))
		else:
			flash("Incorrect user or password")
			app.logger.info("User: "+user+" log in FAILED.")
	return render_template('login.html', title='Log in')
	
@app.route("/signup/", methods=['GET','POST'])
def signup():
	if request.method =='POST':
		name = request.form['name']
		user = request.form['user']
		email = request.form['email']
		pw = request.form['password']
		pw2 = request.form['password2']
		if pw == pw2:
			pwhash = bcrypt.hashpw(pw, bcrypt.gensalt())
			addUser(name, user, email, pwhash)
			app.logger.info("New user registered: "+user+"\t"+email)
			return "Congratulations "+name+"!!! Now you are an user of Snapgram."
			#return redirect(url_for('signupSuccesful', name=name))
		else:
			flash("The passwords don't match.")
	return render_template('signup.html', title='Sign up')

#@app.route("/signup/<name>")
#def signupSuccesful(name):
#	return "Congratulations "+name+"!!! Now you are an user of Snapgram."

@app.route("/")
def root():
	this_route = url_for('.root')
	app.logger.info("Logging a test message from "+this_route)
	return "Root page"

'''
@app.errorhandler(404)
def page_not_found(error):
	return render_template('not_found.html', title='Page not found')
'''
	
@app.route ('/config/')
def config():
	str = []
	str.append('Debug :'+ app.config ['DEBUG'])
	str.append('port :'+ app.config ['port'])
	str.append('url :'+ app.config ['url'])
	str.append('ip_address :'+ app.config ['ip_address'])
	return '\t'. join(str)

def init(app):
	config = ConfigParser.ConfigParser()
	try:
		config_location = "etc/defaults.cfg"
		config.read(config_location)

		app.config['DEBUG'] = config.get("config", "debug")
		app.config['ip_address'] = config.get("config", "ip_address")
		app.config['port'] = config.get("config", "port")
		app.config['url'] = config.get("config", "url")
		
		app.config['log_file'] = config.get("logging", "name")
		app.config['log_location'] = config.get("logging", "location")
		app.config['log_level'] = config.get("logging", "level")
	except:
		print "Could not read configs from : ", config_location

def logs(app):
	log_pathname = app.config['log_location'] + app.config['log_file']
	file_handler = RotatingFileHandler(log_pathname, maxBytes =1024*1024*10, backupCount=1024)
	file_handler.setLevel(app.config['log_level'])
	formatter = logging.Formatter("%(levelname)s | %(asctime)s | %(module)s | %(funcName)s | %(message)s")
	file_handler.setFormatter(formatter)
	app.logger.setLevel(app.config['log_level'])
	app.logger.addHandler(file_handler)


if __name__ == '__main__':
	init(app)
	logs ( app )
	app.run(
		host = app.config['ip_address'],
		port = int(app.config['port']))
		
#if __name__ == "__main__":
#	app.run(host="0.0.0.0", debug = True)
