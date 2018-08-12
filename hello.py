from flask import Flask, render_template, url_for, request, jsonify
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config['MONGO_DBNAME']='bootcamp'
#app.config['MONGO_URI']='mongodb://qasim:qasim@ds143030.mlab.com:43030/miti'
app.config['MONGO_URI']='mongodb://irfan:pass123@ds219532.mlab.com:19532/bootcamp'
mongo = PyMongo(app)


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


@app.route("/users")
def users():
    students=[
        {'id':1, 'name':'Qasim'},
        {'id':2, 'name': 'Zeeshan hanif', 'education':'PHD'}
    ]
    return jsonify({'SaylaniStudents': students})


@app.route("/mongodb")
def mongodb():
    students = []
    records = mongo.db.users.find({'name': 'Muhammad Irfan Afzal'})
    for user in records:
        students.append({'name': user['name']})
    return jsonify({'SaylaniStudents': students})


@app.route("/add")
def add():
    add = mongo.db.users.insert({'name': 'kashan'})
    return "Successfully add"


@app.route("/search", methods=['GET','POST'])
def search():
    if request.method == "POST":
        usearch=request.form['user']
        students=[]
        records = mongo.db.users.find({'name': usearch})
        for user in records:
            students.append({'user': user['name']})
        return jsonify({'SearchData': students})
    else:
        return '''
        <form method="post">
        <h2>Search</h2>
        <input type="text" name="user">
        <input type="submit" value="search">
        </form>
    '''


app.run(debug='true')


