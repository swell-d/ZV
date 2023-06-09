import os

from flask import Flask
from flask_talisman import Talisman

from instance import companies, allianz_unlimited, allianz, barmenia2, barmenia3, diebayerische, muenchenerverein, \
    signaliduna, nuernberger
from routes import error, main_routes

csp = {
    'default-src': "'self'",
    'img-src': ["'self'", 'data:'],
    'style-src': ["'self'", "'unsafe-inline'", 'cdn.jsdelivr.net', '*.fontawesome.com'],
    'script-src': ["'self'", "'unsafe-inline'", 'cdn.jsdelivr.net', '*.fontawesome.com'],
    'connect-src': ["'self'", '*.fontawesome.com'],
    'font-src': ["'self'", '*.fontawesome.com']
}
talisman = Talisman()


def create_app():
    app = Flask(__name__)
    talisman.init_app(app, content_security_policy=csp, session_cookie_samesite='Strict')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or 'my-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 600

    from database import get_db
    db = get_db()
    db.init_app(app)

    error.error_routes(app)
    main_routes.main_routes(app)

    with app.app_context():
        db.create_all()

        companies.create(db)

        allianz_unlimited.create(db)
        allianz.create(db)
        # barmenia1.create(db)
        barmenia2.create(db)
        barmenia3.create(db)
        diebayerische.create(db)
        muenchenerverein.create(db)
        signaliduna.create(db)
        nuernberger.create(db)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
