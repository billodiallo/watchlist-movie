from flask import render_template,redirect,url_for,request,flash
from . import auth
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db
from flask_login import login_user,login_required,logout_user
from ..email import mail_message

@auth.route('/login',methods = ['GET','POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		user = User.query.filter_by(email = form.email.data).first()

		if user is not None and user.verify_password(form.password.data):
			login_user(user,form.remember.data)
			return redirect(request.args.get('next') or url_for('main.index'))

		flash('Invalid username or password')
	
	title = 'Watchlist Login'
	return render_template('auth/login.html',login_form = form,title=title)

@auth.route('/register',methods = ['GET','POST'])
def register():
	form = RegistrationForm()

	if form.validate_on_submit():
		user = User(email = form.email.data, username = form.username.data, password = form.password.data)
		db.session.add(user)
		db.session.commit()
		mail_message('Welcome to Watchlist','email/welcome_user',user.email,user=user)
		return redirect(url_for('auth.login'))
	title = 'New Account'
	return render_template('auth/register.html',registration_form = form, title = title)

	
from flask_login import login_user
from ..models import User
from .forms import LoginForm,RegistrationForm


@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('main.index'))

