from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

from tmdb3 import Movie, set_key, searchMovie, searchPerson, searchStudio
set_key('8756c376f367fb966d3c0dec2c69e1c5')


@app.route("/")
def root():
  #return render_template('base.html', title='Main', pageActive='home')
  return redirect(url_for('movies'))

  
@app.route("/noresults/")
def noresults():
    return render_template('no_results.html', title='No results')

	
@app.route("/movies/", methods=['POST', 'GET'])
def movies():
  if request.method == 'POST':
    keyword = request.form['search field']
    res = searchMovie(keyword)
    if len(res) == 0:
      return redirect(url_for('noresults'))
    else:
      #res.sort(key = lambda movie: movie.popularity)
      #return ',,,'.join(m.title for m in res)  
      return render_template('movies.html', title='Movies', pageActive='movies', movies=res)
  else:
    return render_template('movies.html', title='Movies', pageActive='movies')


@app.route("/people/", methods=['POST', 'GET'])
def people():
  if request.method == 'POST':
    keyword = request.form['search field']
    res = searchPerson(keyword)
    if len(res) == 0:
      return redirect(url_for('noresults'))
    else:
      return render_template('people.html', title='People', pageActive='people', people=res)
  else:
    return render_template('people.html', title='People', pageActive='people')


@app.route("/studios/", methods=['POST', 'GET'])
def studios():
  if request.method == 'POST':
    keyword = request.form['search field']
    res = searchStudio(keyword)
    if len(res) == 0:
      return redirect(url_for('noresults'))
    else:
      return render_template('studios.html', title='Studios', pageActive='studios', studios=res)
  else:
    return render_template('studios.html', title='Studios', pageActive='studios')


@app.route("/contact/")
def contact():
  return render_template('contact.html', title='Contact', pageActive='contact')
  
  
@app.route("/nowplaying/")
def nowplaying():
  movies = Movie.nowplaying()
  res = movies[0:15]
  return render_template('movies.html', title='Now playing | Movies', pageActive='movies', movies=res)


@app.route("/upcoming/")
def upcoming():
  movies = Movie.upcoming()
  res = movies[0:15]
  return render_template('movies.html', title='Upcoming | Movies', pageActive='movies', movies=res)


@app.route("/mostpopular/")
def mostpopular():
  movies = Movie.mostpopular()
  res = movies[0:15]
  return render_template('movies.html', title='Most popular | Movies', pageActive='movies', movies=res)

  
@app.route("/toprated/")
def toprated():
  movies = Movie.toprated()
  res = movies[0:15]
  return render_template('movies.html', title='Top rated | Movies', pageActive='movies', movies=res)


@app.route("/contact/", methods=['POST'])
@app.route("/nowplaying/", methods=['POST'])
@app.route("/upcoming/", methods=['POST'])
@app.route("/mostpopular/", methods=['POST'])
@app.route("/toprated/", methods=['POST'])
@app.route("/noresults/", methods=['POST'])
@app.route("/notfound/", methods=['POST'])
def searchmovies():
  keyword = request.form['search field']
  res = searchMovie(keyword)
  if len(res) == 0:
    return redirect(url_for('noresults'))
  else:
    return render_template('movies.html', title='Movies', pageActive='movies', movies=res)
	

@app.errorhandler(404)
def page_not_found(error):
  return render_template('not_found.html', title='Page not found')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
