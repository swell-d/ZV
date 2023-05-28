import models


def create(db):
    table = """22 
    19,70 
    28,02 
    38,46 
    44 
    25,94 
    39,32 
    56,73 
    23 
    20,07 
    28,65 
    39,47 
    45 
    26,18 
    39,74 
    57,41 
    24 
    20,43 
    29,27 
    40,46 
    46 
    26,41 
    40,16 
    58,08 
    25 
    20,78 
    29,88 
    41,43 
    47 
    26,64 
    40,57 
    58,72 
    26 
    21,11 
    30,47 
    42,38 
    48 
    26,87 
    40,96 
    59,35 
    27 
    21,44 
    31,04 
    43,31 
    49 
    27,10 
    41,35 
    59,96 
    28 
    21,75 
    31,60 
    44,21 
    50 
    27,32 
    41,72 
    60,54 
    29 
    22,05 
    32,15 
    45,09 
    51 
    27,53 
    42,08 
    61,09 
    30 
    22,34 
    32,68 
    45,95 
    52 
    27,74 
    42,42 
    61,62 
    31 
    22,62 
    33,20 
    46,80 
    53 
    27,94 
    42,75 
    62,12 
    32 
    22,90 
    33,71 
    47,63 
    54 
    28,13 
    43,06 
    62,59 
    33 
    23,17 
    34,21 
    48,44 
    55 
    28,31 
    43,35 
    63,02 
    34 
    23,43 
    34,70 
    49,25 
    56 
    28,48 
    43,62 
    63,43 
    35 
    23,70 
    35,19 
    50,04 
    57 
    28,65 
    43,86 
    63,80 
    36 
    23,96 
    35,67 
    50,82 
    58 
    28,81 
    44,10 
    64,14 
    37 
    24,21 
    36,15 
    51,60 
    59 
    28,89 
    44,21 
    64,29 
    38 
    24,47 
    36,62 
    52,36 
    60 
    28,96 
    44,31 
    64,41 
    39 
    24,72 
    37,08 
    53,11 
    61 
    29,02 
    44,38 
    64,50 
    40 
    24,97 
    37,54 
    53,86 
    62 
    29,07 
    44,43 
    64,54 
    41 
    25,21 
    38,00 
    54,59 
    63 
    29,11 
    44,45 
    64,55 
    42 
    25,46 
    38,44 
    55,32 
    64 
    29,17 
    44,51 
    64,62 
    43 
    25,70 
    38,88 
    56,03 
    65 
    29,20 
    44,53 
    64,62""".split('\n')

    allianz = models.Company.query.filter_by(short_name='allianz').first()

    tarif1 = models.Tariff(
        name='MeinZahnschutz 75 (ZS75AR)',
        company=allianz,
        unlimited=1,
        description=''
    )
    db.session.add(tarif1)

    tarif2 = models.Tariff(
        name='MeinZahnschutz 90 (ZS90AR)',
        company=allianz,
        unlimited=1,
        description=''
    )
    db.session.add(tarif2)

    tarif3 = models.Tariff(
        name='MeinZahnschutz 100 (ZS100AR)',
        company=allianz,
        unlimited=1,
        description=''
    )
    db.session.add(tarif3)

    for i in range(int(len(table) / 4)):
        a1 = int(table[i * 4 + 0].strip().replace(',', '.'))
        a2 = float(table[i * 4 + 1].strip().replace(',', '.'))
        a3 = float(table[i * 4 + 2].strip().replace(',', '.'))
        a4 = float(table[i * 4 + 3].strip().replace(',', '.'))

        new = models.Condition(
            tariff=tarif1,
            min_age=a1,
            max_age=a1,
            price=a2
        )
        db.session.add(new)

        new = models.Condition(
            tariff=tarif2,
            min_age=a1,
            max_age=a1,
            price=a3
        )
        db.session.add(new)

        new = models.Condition(
            tariff=tarif3,
            min_age=a1,
            max_age=a1,
            price=a4
        )
        db.session.add(new)

    db.session.commit()
