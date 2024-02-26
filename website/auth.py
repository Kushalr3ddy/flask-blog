__package__ = "website"
from flask import Blueprint,render_template,redirect,url_for,request,flash

from . import db
from .models import User
from flask_login import login_user,logout_user,login_required,current_user
from werkzeug.security import generate_password_hash,check_password_hash

auth = Blueprint("auth",__name__)

@auth.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":

        email= request.form.get("email")
        password= request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('logged in ',category='success')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('password is incorrect',category='error')
        else:
            flash('email does not exist',category='error')
    return render_template("login.html",user=current_user)





@auth.route("/sign-up",methods=["GET","POST"])
def signup():
    if request.method == "POST":
        email= request.form.get("email")
        username= request.form.get("username")
        password1= request.form.get("password1")
        password2= request.form.get("password2")
        
        email_exists=User.query.filter_by(email=email).first()# the first part doesnt matter cause we are taking in unique values for email in database itself
        username_exists=User.query.filter_by(username=username).first()
        
        if email_exists:
            flash("email already in use",category='error')
        elif username_exists:
            flash('This username is already taken',category='error')
        elif password1 != password2:
            flash('The passwords do not match',category='error')
        elif len(username) < 2:
            flash('Username too short',category='error')
        elif len(password1) < 6:
            flash('Password is too short',category='error')
        elif len(email) < 4:
            flash('email is invalid',category='error')
        else:
            new_user = User(email=email,username=username,password=generate_password_hash(password1,method='scrypt'))
            db.session.add(new_user)
            db.session.commit()
            flash('User created')
            login_user(new_user,remember=True)
            return redirect(url_for('views.home'))


    #print(username)
    return render_template("signup.html",user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))