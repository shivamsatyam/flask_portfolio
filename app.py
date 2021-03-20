from flask import Flask, render_template,jsonify,request, session, redirect,flash
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
import htmlentities
import datetime
from bson.objectid import ObjectId


client = MongoClient("mongodb://localhost:27017/")
database = client['portfolio']

bcrypt = Bcrypt()

app = Flask(__name__)
app.secret_key = 'super-secret-key'


@app.route('/')
def home():
	return render_template('main.html')

@app.route('/content')
def content():
	if("email" in session):

		return render_template('index.html',session=session)
	else:
		return redirect('/')	

@app.route('/auth')
def auth():
	return render_template('home.html')

@app.route('/signin', methods=['GET', 'POST'])
def siginin():
	if request.method=="POST":
		username = request.form.get('username')
		password = request.form.get('password')
		email = request.form.get('email')

		password_hash = bcrypt.generate_password_hash(str(password))
		no_of_user  = database.person.count_documents({"email":email})
		if no_of_user==0:
			record = {"username":str(htmlentities.encode(username)),"password":password_hash,"email":email}

			database.person.insert_one(record)

			flash("the insertion occur succesfully","danger")
		else:

			flash("The email is already in use","danger")

		


	return render_template('home.html')




@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method=="POST":
		
		password = request.form.get('password')
		email = request.form.get('email')

		no_of_user = database.person.count_documents({"email":email})

		if no_of_user==1:
			data = database.person.find({"email":email})[0]
			if (data['email'] == email) and (bcrypt.check_password_hash(data['password'],password)):
				session['email'] = email
				session['username'] = data['username']
				flash("You login succesfully","danger") 
		else:
			flash("Please signin first","danger")	


	return render_template('home.html')


@app.route('/save', methods=['POST'])
def save():
	
	try:
		email = session['email']
		username = session['username']
		print(request)
		data = request.get_json()['data']
		with open ("a.txt",'w') as op:
			op.write(str(request.get_json))

		database.content.insert_one({"username":username,"email":email,"content":htmlentities.encode(data),"title":request.get_json()['title'],"desc":request.get_json()['desc']})
		return jsonify({"status":True})

	except Exception as e:
		return jsonify({"status":False})	
	
		

@app.route('/your')

def your():
	if ("email" in session):
		data = database.content.find({"email":session['email']})
		return render_template('your.html',data=data)	

	else:
		return redirect('/auth')	



@app.route('/portfolio/<string:search_id>')
def portfolio(search_id):
	data = database.content.find({"_id":ObjectId(search_id)})[0]

	
	return render_template('show.html',data = data['content'])
		



app.run(debug=True)