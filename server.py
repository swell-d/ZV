import os

from flask import Flask
from flask_wtf import CSRFProtect

from instance import companies, allianz_unlimited, allianz, barmenia2, barmenia3, diebayerische
from routes import error, main_routes

csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    csrf.init_app(app)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or 'my-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

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

    @app.after_request
    def add_header(response):
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['Content-Security-Policy'] = \
            "default-src 'self'; " \
            "img-src 'self' data: ; " \
            "style-src 'self' 'unsafe-inline' cdn.jsdelivr.net *.fontawesome.com; " \
            "script-src 'self' 'unsafe-inline' cdn.jsdelivr.net *.fontawesome.com; " \
            "connect-src 'self' *.fontawesome.com; " \
            "font-src 'self' *.fontawesome.com;"
        return response

    return app


if __name__ == '__main__':
    create_app().run(debug=False)
