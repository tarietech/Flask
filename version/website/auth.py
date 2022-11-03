import email 
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('veiws.home'))
            else: 
                flash('Incorrect password, try again', category='error')

        else: 
            flash('Email does not exist.', category='error')




    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    

    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        surname = request.form.get('surname')
        userName = request.form.get('userName')
        password1 = request.form.get('password1')
        password2 =request.form.get('password2')
 
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4', category='error')
        elif    len(first_name) < 2: 
            flash('firstName must be greater than 2 characters',category="error") 

        elif password1  != password2:
            flash('passwords dont match',category="error")

        elif len(userName) < 6:
            flash('username is too short at least 6 characters :)',category="error")
        elif len(password1) < 8:
            flash('pass phrase is too short and weak it should contain characters like .+*#,/1 uppercase and lowercase ',category="error")

        elif len(password2) < 8:
            flash('pass phrase is too short and weak it should contain characters like .+*#,/1 uppercase and lowercase ',category="error")
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created ', category='success')
            return redirect(url_for('veiws.home'))
            
             
    return render_template("sign_up.html")      

@auth.route('/market')
def market():
    return render_template("market.html")

@auth.route('/inventory')
def inventory():
    return render_template("inventory.html")
     