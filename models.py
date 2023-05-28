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


class Tariff(db.Model):
    __tablename__ = 'tariffs'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=func.now())
    name = db.Column(db.String(100), nullable=False)
    mode = db.Column(db.Integer, default=1)  # 0-disable  1-enable
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    company = db.relationship("Company", backref="tariffs")
    unlimited = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000))


class Condition(db.Model):
    __tablename__ = 'conditions'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=func.now())
    mode = db.Column(db.Integer, default=1)  # 0-disable  1-enable
    tariff_id = db.Column(db.Integer, db.ForeignKey('tariffs.id'), nullable=False)
    tariff = db.relationship("Tariff", backref="conditions")
    min_age = db.Column(db.Integer, nullable=False)
    max_age = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
