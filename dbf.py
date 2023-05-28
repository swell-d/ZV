import database
import models

db = database.get_db()


def commit():
    db.session.commit()


def get_all_companies():
    return models.Company.query.all()


def get_companies(names):
    return [models.Company.query.filter_by(name=name).first() for name in names]


def get_conditions(company_short_name, age):
    company = models.Company.query.filter_by(short_name=company_short_name).first()

    result = []
    for tariff in company.tariffs:
        for condition in tariff.conditions:
            if condition.min_age <= age and condition.max_age >= age:
                result.append(condition)
    return result
