import database
import models

db = database.get_db()


def commit():
    db.session.commit()


def get_user_by_id(user_id):
    return models.User.query.filter_by(id=user_id).first()


def get_user_by_email(email):
    return models.User.query.filter_by(email=email).first()


def delete_user(user_id):
    models.User.query.filter_by(id=user_id).delete()
    db.session.commit()


def get_all_companies():
    return models.Company.query.all()


def get_companies(names):
    return [models.Company.query.filter_by(name=name).first() for name in names]
