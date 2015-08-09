from bottle import Bottle, run, template


app = Bottle()

@app.route('/hello')
def hello():
	return "Hello world!"

@app.route('/')
@app.route('/hello/<name>')
def greeting(name='Stranger'):
	return template('Hello {{name}}, how are you?', name=name)

@app.route('/<firstname>/<lastname>')
def greeting_two(firstname='unknown', lastname='person'):
	return template('Hello {{firstname}} {{lastname}}, how are you?',
		firstname=firstname, lastname=lastname)

app.run(host='localhost', port=8080, debug=True)