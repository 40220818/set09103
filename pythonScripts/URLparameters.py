from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def root():
  return 'root route'

@app.route("/hello/")
def hello():
  name = request.args.get('name','')
  if name == '':
    return 'no param supplied'
  else:
    return 'Hello %s' % name

@app.route("/add/<int:first>/<int:second>")
def add(first, second):
  return str(first+second)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
