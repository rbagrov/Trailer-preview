from flask import Flask, render_template, url_for, request
import syslog
from db import DB

'''
One variable definition and flask instantiation.
'''
pname = 'Trailer preview'
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
	'''
	The only view we have. All in one page, where we check if user GETs or POSTs.
	If user is POSTing we create a single list and append each from element into it.
	Very important here is the sequence, since we are using it in the DB api.
	When we get all data from the user we execute same procedure we do in GET:
	- get all data and render out main html with it.
	'''
	api = DB()
	if request.method == 'POST':
		new_movie = []
		_title = request.form.get('title')
		new_movie.append(_title)
		_story = request.form.get('story')
		new_movie.append(_story)
		_poster = request.form.get('poster')
		new_movie.append(_poster)
		_trailer = request.form.get('trailer')
		new_movie.append(_trailer)
		_cast = request.form.get('cast')
		new_movie.append(_cast)
		api.add(new_movie)
		result = api.get_data()
		return render_template("index.html", pname=pname, result=result)
	result = api.get_data()
	return render_template("index.html", pname=pname, result=result)

if __name__ == "__main__":
	syslog.syslog('Starting ' + pname + '...')
	app.run(host='0.0.0.0', port=8111, debug=True)
