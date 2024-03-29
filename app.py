from flask import Flask ,render_template,request,redirect,session
from db import Database
import api

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
dbo = Database()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration',methods=['POST'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = dbo.insert(name,email,password)
    if response:
        return render_template('login.html', message="Registration successful. Kindly login to proceed")
    else:
        return render_template('register.html',message="Email Already Exists.")

@app.route('/perform_login',methods=['POST'])
def perform_login():

    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = dbo.search(email,password)

    if response:
        session["logged_in"] = 1
        return redirect('/profile')
    else:
        return render_template('login.html',message="Invalid Email or Password.")

@app.route('/profile')
def profile():
    if 'logged_in' in session:
        return render_template('profile.html')
    else:
        redirect('/')

@app.route('/ner')
def ner():
    if 'logged_in' in session:
        return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform_ner',methods=['POST'])
def perform_ner():
    if 'logged_in' in session:
        text = request.form.get('ner_text')
        response = api.ner(text)
        return render_template('ner.html', response=response)
    else:
        return redirect('/')


app.run(debug=True,port=8080)