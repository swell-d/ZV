import models


def create(db):
    table = """0-15 
    5,70 
    19,00 
    21,10 
    22,00 
    16-20 
    7,50 
    16,30 
    18,60 
    19,40 
    21-25
    15,00 
    21,50 
    27,00 
    27,20 
    26-30
    15,00 
    21,50 
    27,00 
    27,20 
    31-35
    15,00 
    21,50  
    35,20 
    36,50 
    36-40 
    19,40 
    28,20
    35,20 
    36,50 
    41-45 
    21,90 
    31,90 
    44,70 
    46,10 
    46-50 
    24,50 
    35,70 
    50,50 
    52,60 
    51-55 
    27,90 
    41,00 
    58,80 
    61,60 
    56-60 
    30,50 
    44,80 
    64,70 
    68,70 
    61-65 
    33,30 
    49,10 
    71,50 
    76,70 
    66-70 
    34,00 
    50,10 
    72,90 
    78,50 
    71-75 
    33,00 
    48,60 
    70,80 
    76,70 
    76-80 
    31,70 
    46,80 
    68,40 
    74,50 
    81-85 
    24,70 
    36,30 
    53,10 
    58,20 
    86-99
    17,60 
    26,00 
    37,90 
    42,40""".split('\n')

    diebayerische = models.Company.query.filter_by(short_name='diebayerische').first()

    tarif1 = models.Tariff(
        name='ZAHN Smart',
        company=diebayerische,
        unlimited=0,
        prosthodontics=80,
        description=''
    )
    db.session.add(tarif1)

    tarif2 = models.Tariff(
        name='ZAHN Komfort',
        company=diebayerische,
        unlimited=0,
        prosthodontics=90,
        description=''
    )
    db.session.add(tarif2)

    tarif3 = models.Tariff(
        name='ZAHN Prestige',
        company=diebayerische,
        unlimited=0,
        prosthodontics=100,
        description=''
    )
    db.session.add(tarif3)

    tarif4 = models.Tariff(
        name='ZAHN Prestige Plus',
        company=diebayerische,
        unlimited=0,
        prosthodontics=100,
        description=''
    )
    db.session.add(tarif4)

    # tarif5 = models.Tariff(
    #     name='ZAHN Sofort',
    #     company=diebayerische,
    #     unlimited=0,
    #     prosthodontics=0,
    #     description=''
    # )
    # db.session.add(tarif5)

    cycle = 5
    for i in range(int(len(table) / cycle)):
        a1 = table[i * cycle + 0].strip().replace(',', '.')
        a2 = float(table[i * cycle + 1].strip().replace(',', '.'))
        a3 = float(table[i * cycle + 2].strip().replace(',', '.'))
        a4 = float(table[i * cycle + 3].strip().replace(',', '.'))
        a5 = float(table[i * cycle + 4].strip().replace(',', '.'))

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

        new = models.Condition(
            tariff=tarif4,
            min_age=int(a1.split('-')[0]),
            max_age=int(a1.split('-')[1]),
            price=a5
        )
        db.session.add(new)

    # new = models.Condition(
    #     tariff=tarif5,
    #     min_age=0,
    #     max_age=99,
    #     price=29.90
    # )
    # db.session.add(new)

    db.session.commit()
