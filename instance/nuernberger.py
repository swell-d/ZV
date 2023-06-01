import models


def create(db):
    table = """0-20	12,0	15,0	18,5
    21-30	15,5	19,5	23,5
    31-40	22,0	28,0	33,0
    41-45	28,0	35,5	42,5
    46-50	33,0	42,0	50,0
    51-55	39,0	49,0	58,5
    56-60	44,5	56,0	67,0
    61-99	53,5	67,0	80,5""".split('\n')

    nuernberger = models.Company.query.filter_by(short_name='nuernberger').first()

    tarif1 = models.Tariff(
        name='Komfort 80 (Z80)',
        company=nuernberger,
        unlimited=0,
        prosthodontics=80,
        orto=0,
        description=''
    )
    db.session.add(tarif1)

    tarif2 = models.Tariff(
        name='Komfort 90 (Z90)',
        company=nuernberger,
        unlimited=0,
        prosthodontics=90,
        orto=0,
        description=''
    )
    db.session.add(tarif2)

    tarif3 = models.Tariff(
        name='Komfort 100 (Z100)',
        company=nuernberger,
        unlimited=0,
        prosthodontics=100,
        orto=0,
        description=''
    )
    db.session.add(tarif3)

    for each in table:
        a0 = each.strip().split('	')[0]
        a1 = float(each.strip().split('	')[1].replace(',', '.'))
        a2 = float(each.strip().split('	')[2].replace(',', '.'))
        a3 = float(each.strip().split('	')[3].replace(',', '.'))

        new = models.Condition(
            tariff=tarif1,
            min_age=int(a0) if '-' not in a0 else int(a0.split('-')[0]),
            max_age=int(a0) if '-' not in a0 else int(a0.split('-')[1]),
            price=a1
        )
        db.session.add(new)

        new = models.Condition(
            tariff=tarif2,
            min_age=int(a0) if '-' not in a0 else int(a0.split('-')[0]),
            max_age=int(a0) if '-' not in a0 else int(a0.split('-')[1]),
            price=a2
        )
        db.session.add(new)

        if a3:
            new = models.Condition(
                tariff=tarif3,
                min_age=int(a0) if '-' not in a0 else int(a0.split('-')[0]),
                max_age=int(a0) if '-' not in a0 else int(a0.split('-')[1]),
                price=a3
            )
            db.session.add(new)

    db.session.commit()
