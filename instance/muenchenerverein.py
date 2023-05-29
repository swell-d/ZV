import models


def create(db):
    table1 = """0-5 1,00 
    6-15 2,50 
    16-25 7,90 
    26-30 12,90 
    31-35 12,90 
    36-40 16,90 
    41-45 18,90 
    46-50 18,90 
    51-55 24,90 
    56-60 27,90 
    61-99 35,90""".split('\n')
    table2 = """0-5 1,10 
    6-15 3,00 
    16-25 9,90 
    26-30 17,90 
    31-35 17,90 
    36-40 20,90 
    41-45 25,90 
    46-50 27,90 
    51-55 32,90 
    56-60 42,90 
    61-99 50,90""".split('\n')
    table3 = """0-5 1,50 
    6-15 13,30 
    16-25 16,60 
    26-30 24,80 
    31-35 31,80 
    36-40 37,90 
    41-45 37,90 
    46-50 47,90 
    51-55 54,40 
    56-60 71,90 
    61-99 79,90""".split('\n')

    muenchenerverein = models.Company.query.filter_by(short_name='muenchenerverein').first()

    tarif1 = models.Tariff(
        name='ZahnGesund 75+',
        company=muenchenerverein,
        unlimited=0,
        prosthodontics=75,
        description=''
    )
    db.session.add(tarif1)

    tarif2 = models.Tariff(
        name='ZahnGesund 85+',
        company=muenchenerverein,
        unlimited=0,
        prosthodontics=85,
        description=''
    )
    db.session.add(tarif2)

    tarif3 = models.Tariff(
        name='ZahnGesund 100',
        company=muenchenerverein,
        unlimited=0,
        prosthodontics=100,
        description=''
    )
    db.session.add(tarif3)

    for each in table1:
        a1 = each.strip().split(' ')[0].split('-')[0]
        a2 = each.strip().split(' ')[0].split('-')[1]
        a3 = float(each.strip().split(' ')[1].replace(',', '.'))

        new = models.Condition(
            tariff=tarif1,
            min_age=int(a1),
            max_age=int(a2),
            price=a3
        )
        db.session.add(new)

    for each in table2:
        a1 = each.strip().split(' ')[0].split('-')[0]
        a2 = each.strip().split(' ')[0].split('-')[1]
        a3 = float(each.strip().split(' ')[1].replace(',', '.'))

        new = models.Condition(
            tariff=tarif2,
            min_age=int(a1),
            max_age=int(a2),
            price=a3
        )
        db.session.add(new)

    for each in table3:
        a1 = each.strip().split(' ')[0].split('-')[0]
        a2 = each.strip().split(' ')[0].split('-')[1]
        a3 = float(each.strip().split(' ')[1].replace(',', '.'))

        new = models.Condition(
            tariff=tarif3,
            min_age=int(a1),
            max_age=int(a2),
            price=a3
        )
        db.session.add(new)

    db.session.commit()
