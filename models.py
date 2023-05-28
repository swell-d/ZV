from sqlalchemy import func

import database

db = database.get_db()


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
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    company = db.relationship("Company", back_populates="tariffs")
    name = db.Column(db.String(100), nullable=False)
    mode = db.Column(db.Integer, default=1)  # 0-disable  1-enable
    min_age = db.Column(db.Integer, nullable=False)
    max_age = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    conditions = db.Column(db.String(1000))
