from flask import Flask, request, render_template
app = Flask(__name__)

##from tmdb3 import set_key, searchMovie
##set_key('8756c376f367fb966d3c0dec2c69e1c5')

@app.route("/")
def root():
  return render_template('base.html')

@app.route("/movies/", methods=['POST', 'GET'])
def movies():
  if request.method == 'POST':
    keyword = request.form['keyword']
    return res
    ##res = searchMovie(keyword)
    ##print res
    ##return res[0]
  else:
    return render_template('movies.html')

@app.route("/people/")
def people():
  return render_template('people.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
