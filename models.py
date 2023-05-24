from flask_login import UserMixin
from sqlalchemy import func

import database

db = database.get_db()


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=func.now())
    email = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Integer)


class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=func.now())
    name = db.Column(db.String(100), nullable=False, unique=True)
    short_name = db.Column(db.String(100), nullable=False, unique=True)
    mode = db.Column(db.Integer, default=1)  # 0-disable  1-enable
    logo = db.Column(db.String(100))
    short_description = db.Column(db.String(1000))
    tariffs = db.relationship('Tariff', back_populates='company')


class Tariff(db.Model):
    __tablename__ = 'tariffs'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=func.now())
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    company = db.relationship("Company", back_populates="tariffs")
    name = db.Column(db.String(100), nullable=False, unique=True)
    mode = db.Column(db.Integer, default=0)  # 0-disable  1-enable
    conditions = db.Column(db.String(1000))
