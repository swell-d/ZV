import database
import models

db = database.get_db()


def commit():
    db.session.commit()


def get_all_companies():
    return models.Company.query.all()


def get_companies(names):
    return [models.Company.query.filter_by(name=name).first() for name in names]


def get_tariffs(company_short_name, age):
    company = models.Company.query.filter_by(short_name=company_short_name).first()
    return [tariff for tariff in company.tariffs if tariff.min_age <= age and tariff.max_age >= age]
