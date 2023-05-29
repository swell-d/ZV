import models


def create(db):
    table = """0-20 
    15,70 
    16,00 
    16,30 
    21-30 
    13,60 
    16,10 
    18,50 
    31-40 
    19,60 
    25,80 
    31,50 
    41-50 
    24,90 
    34,10 
    42,70 
    51-60 
    32,90 
    46,50 
    59,40 
    61-99
    38,20 
    54,70 
    70,40""".split('\n')

    barmenia = models.Company.query.filter_by(short_name='barmenia').first()

    tarif1 = models.Tariff(
        name='Mehr Zahn 80, Mehr Zahnvorsorge Bonus',
        company=barmenia,
        unlimited=0,
        prosthodontics=80,
        description=''
    )
    db.session.add(tarif1)

    tarif2 = models.Tariff(
        name='Mehr Zahn 90, Mehr Zahnvorsorge Bonus',
        company=barmenia,
        unlimited=0,
        prosthodontics=90,
        description=''
    )
    db.session.add(tarif2)

    tarif3 = models.Tariff(
        name='Mehr Zahn 100, Mehr Zahnvorsorge Bonus',
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
