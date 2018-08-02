from flask import Flask, render_template, url_for, request

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


@app.route("/form")
def form():
    return ''' 
<form action="/info" method="POST">
<input type="text" name="user" placeholder="Full Name"><br>
<input type="email" name="email" placeholder="Email"><br>
<input type="password" name="pass" placeholder="password"><br>
<input type="submit" value="Send">
</form>
'''

@app.route("/info", methods=['GET','POST'])
def info():
    if request.method == "GET":
        return "<h1>GET Method</h1> Hello "+ request.args.get('user') + \
    " <br> Your Email: "+request.args.get('email') + \
    " <br> Your password: "+request.args.get('pass')
    else:
        return "<h1>POST Method</h1>Hello "+ request.form['user'] + \
    " <br> Your Email: "+request.form['email'] + \
    " <br> Your password: " + request.form['pass']


app.run(debug='true')


