from flask import render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

import database
import dbf
import models
from main import send_email


def auth_routes(app):
    db = database.get_db()

    @app.route('/login', methods=['GET'])
    def login():
        data = {'title': 'Login'}
        return render_template('auth/login.html', **data)

    @app.route('/login', methods=['POST'])
    def login_post():
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = models.User.query.filter_by(email=email).first()

        if not user:
            flash('Email address not found. Please check your login details and try again.')
            return redirect(url_for('login'))
        if not check_password_hash(user.password, password):
            flash('Wrong password. Please check your login details and try again.')
            return redirect(url_for('login'))

        login_user(user, remember=remember)
        return redirect(url_for('home'))

    @app.route('/signup', methods=['GET'])
    def signup():
        data = {'title': 'Sing up'}
        return render_template('auth/signup.html', **data)

    @app.route('/signup', methods=['POST'])
    def signup_post():
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        if models.User.query.filter_by(email=email).first():
            flash('Email address already exists. Please, login')
            return redirect(url_for('login'))

        new_user = models.User(email=email,
                               name=name,
                               password=generate_password_hash(password),
                               admin=None if models.User.query.first() else 1
                               )
        db.session.add(new_user)
        db.session.commit()

        try:
            send_email.new_user(new_user)
        except ConnectionRefusedError:
            pass
        login_user(new_user, remember=False)

        return redirect(url_for('home'))

    @app.route('/profile', methods=['GET'])
    @login_required
    def profile():
        data = {'title': 'Profile'}
        return render_template('auth/profile.html', **data)

    @app.route('/profile', methods=['POST'])
    @login_required
    def delete_user():
        dbf.delete_user(user_id=current_user.id)
        return redirect(url_for('home'))

    @app.route('/logout', methods=['GET'])
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('home'))
