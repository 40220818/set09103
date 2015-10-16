from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def root():
  return 'root route'

@app.route("/hello/")
def hello():
  return 'hello'

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
