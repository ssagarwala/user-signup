#!/usr/bin/python
from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2
import re

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route('/validate-form', methods=['POST'])
def validate_form():
    #name = "abcdefghijklmnopqrstuv"
    name = request.form['name']
    password = request.form['password']
    passmatch = request.form['passmatch']
    email=request.form['email']

    name_error = '' 
    password_error = ''
    passmatch_error= ''
    email_error=''
    pattern = re.compile('[a-zA-Z0-9]{3,20}@[a-zA-Z0-9]+\.[a-zA-Z0-9]+')
    


    if (len(name) < 3)  or (len(name) >20) or (len(name) ==0) or (not name.isalpha()):
        name_error = 'Please enter your name - name length [3-20] - No space is allowed'
        name=name
        
    if (len(password) < 3)  or (len(password) >20) or (len(password) ==0) or (not password.isalpha()):
        password_error = 'Please enter your password - password length [3-20] - No space is allowed'
        password=''
    if not (password == passmatch):
        passmatch_error="Passwords do not match"
        passmatch=''
    
    if (len(email)>0 ) and not pattern.match(email):
        email_error="Please provide valid email"
        email=email
   
    if not name_error and not password_error and not passmatch_error and not email_error:
           template = jinja_env.get_template('welcome.html')
           return template.render(name=name)
    else:
        template = jinja_env.get_template('index.html')
        return template.render(name_error=name_error,name=name,password=password,password_error=password_error,
                                passmatch=passmatch,passmatch_error=passmatch_error,email_error=email_error,email=email)

@app.route("/")
def index():
    #encoded_error = request.args.get("error")
    return render_template('index.html') #, error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()