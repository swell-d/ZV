import models


def create(db):
    table = """0-20 
    8,43 
    13,15 
    17,47 
    21-30 
    12,94 
    15,89 
    18,77 
    31-40 
    17,39 
    23,58 
    29,88 
    41-50 
    21,55 
    31,56 
    41,73 
    51-60 
    27,10 
    41,89 
    56,93 
    61-99 
    30,64 
    48,04 
    65,63""".split('\n')

    allianz = models.Company.query.filter_by(short_name='allianz').first()

    tarif1 = models.Tariff(
        name='MeinZahnschutz 75 (ZS75)',
        company=allianz,
        unlimited=0,
        prosthodontics=75,
        description=''
    )
    db.session.add(tarif1)

    tarif2 = models.Tariff(
        name='MeinZahnschutz 90 (ZS90)',
        company=allianz,
        unlimited=0,
        prosthodontics=90,
        description=''
    )
    db.session.add(tarif2)

    tarif3 = models.Tariff(
        name='MeinZahnschutz 100 (ZS100)',
        company=allianz,
        unlimited=0,
        prosthodontics=100,
        description=''
    )
    db.session.add(tarif3)

    for i in range(int(len(table) / 4)):
        a1 = table[i * 4 + 0].strip().replace(',', '.')
        a2 = float(table[i * 4 + 1].strip().replace(',', '.'))
        a3 = float(table[i * 4 + 2].strip().replace(',', '.'))
        a4 = float(table[i * 4 + 3].strip().replace(',', '.'))

        new = models.Condition(
            tariff=tarif1,
            min_age=a1.split('-')[0],
            max_age=a1.split('-')[1],
            price=a2
        )
        db.session.add(new)

        new = models.Condition(
            tariff=tarif2,
            min_age=a1.split('-')[0],
            max_age=a1.split('-')[1],
            price=a3
        )
        db.session.add(new)

        new = models.Condition(
            tariff=tarif3,
            min_age=a1.split('-')[0],
            max_age=a1.split('-')[1],
            price=a4
        )
        db.session.add(new)

    db.session.commit()
