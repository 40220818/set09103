from flask import Flask
app = Flask(__name__)

@app.route("/")
def sum():
  x = 1+1
  return 'root route'+str(x)

@app.route("/napier/")
def hello2():
  return 'Hello Napier!'

@app.route("/bye/")
def bye():
  return 'Goodbye world'

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
