import database
import models

db = database.get_db()


def commit():
    db.session.commit()


def get_all_companies():
    return models.Company.query.all()


def get_companies(names):
    return [models.Company.query.filter_by(name=name).first() for name in names]


def get_conditions(company_short_name, age, teeth, prosthodontics, prosthodontics_full, orto, unlimited):
    company = models.Company.query.filter_by(short_name=company_short_name).first()

    result = []
    for tariff in company.tariffs:
        if not tariff.mode: continue

        if unlimited and not tariff.unlimited: continue
        if not unlimited and tariff.unlimited: continue

        if prosthodontics_full and tariff.prosthodontics != 100: continue
        if not prosthodontics_full and tariff.prosthodontics == 100: continue

        for condition in tariff.conditions:
            if not condition.mode: continue
            if condition.min_age <= age <= condition.max_age:
                result.append(condition)

    return result
