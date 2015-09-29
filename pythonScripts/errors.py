from flask import Flask, abort
app = Flask(__name__)

@app.route("/")
def hello():
  return 'Hello World!'


@app.route("/throw")
def force():
  abort(405)

@app.errorhandler(404)
def pageNotFound(error):
  return "Couldn't get the page you requested", 404


@app.errorhandler(405)
def pageNotFound(error):
  return "throwed error 405", 405

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
