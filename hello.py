from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return 'About Us page'


@app.route('/user/<username>')
def user(username):
    return 'Hello Dear: '+username

app.run(debug='true')


