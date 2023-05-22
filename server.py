import os

from flask import Flask
from flask_babel import Babel
from flask_login import LoginManager
from flask_wtf import CSRFProtect

import models
from routes import error, admin, auth, main_routes

csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    csrf.init_app(app)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or 'my-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    from database import get_db
    db = get_db()
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(models.User, int(user_id))

    error.error_routes(app)
    main_routes.main_routes(app)
    auth.auth_routes(app)
    admin.admin_routes(app)

    with app.app_context():
        db.create_all()

    babel = Babel(app)

    return app


if __name__ == '__main__':
    create_app().run(debug=False)
