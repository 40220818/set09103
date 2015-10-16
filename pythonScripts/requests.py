from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def root():
  return 'root route'

@app.route("/account/", methods=['GET', 'POST'])
def account():
  if request.method == 'POST':
    return request.method+"'ed to /account root"
  else:
    return request.method+" /account root"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
