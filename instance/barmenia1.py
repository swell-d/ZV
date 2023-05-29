import models


def create(db):
    table = """0-20 
    0,70 
    1,00 
    1,30 
    21-30 
    4,60 
    7,10 
    9,50 
    31-40 
    10,60 
    16,80 
    22,50 
    41-50 
    15,90 
    25,10 
    33,70 
    51-60 
    23,90 
    37,50 
    50,40 
    61-99
    29,20 
    45,70 
    61,40""".split('\n')

    barmenia = models.Company.query.filter_by(short_name='barmenia').first()

    tarif1 = models.Tariff(
        name='Mehr Zahn 80',
        company=barmenia,
        unlimited=0,
        prosthodontics=80,
        description=''
    )
    db.session.add(tarif1)

    tarif2 = models.Tariff(
        name='Mehr Zahn 90',
        company=barmenia,
        unlimited=0,
        prosthodontics=90,
        description=''
    )
    db.session.add(tarif2)

    tarif3 = models.Tariff(
        name='Mehr Zahn 100',
        company=barmenia,
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
            min_age=int(a1.split('-')[0]),
            max_age=int(a1.split('-')[1]),
            price=a2
        )
        db.session.add(new)

        new = models.Condition(
            tariff=tarif2,
            min_age=int(a1.split('-')[0]),
            max_age=int(a1.split('-')[1]),
            price=a3
        )
        db.session.add(new)

        new = models.Condition(
            tariff=tarif3,
            min_age=int(a1.split('-')[0]),
            max_age=int(a1.split('-')[1]),
            price=a4
        )
        db.session.add(new)

    db.session.commit()
