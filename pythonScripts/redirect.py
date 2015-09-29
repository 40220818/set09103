from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/private")
def private():
  #test of login failed, so redirect to login UEL
  return redirect(url_for('login'))

@app.route("/login")
def login():
  return "Put your username and password"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
