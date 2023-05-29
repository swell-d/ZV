import models


def create(db):
    table = """0-19	3,5	7	0	11,59	0	22,89	0
    20	4,4	10,36	17,6	14,32	25,55	23,17	41,85
    21	4,4	10,36	18,06	14,32	26,28	23,17	42,44
    22	4,4	10,36	18,54	14,32	27,04	23,17	43,16
    23	4,4	10,36	19,04	14,32	27,8	23,17	44,03
    24	4,4	10,36	19,54	14,32	28,58	23,17	44,86
    25	4,4	10,36	20,04	14,32	29,35	23,17	45,68
    26	4,4	10,36	20,54	14,32	30,11	23,17	46,46
    27	4,4	10,36	21,03	14,32	30,86	23,17	47,22
    28	4,4	10,36	21,52	14,32	31,59	23,17	47,96
    29	4,4	10,36	21,99	14,32	32,31	23,17	48,68
    30	4,4	10,36	22,46	14,32	33,01	29,99	49,4
    31	4,4	10,36	22,91	14,32	33,7	29,99	50,12
    32	4,4	10,36	23,36	14,32	34,37	29,99	50,83
    33	4,4	10,36	23,79	14,32	35,02	29,99	51,53
    34	4,4	10,36	24,21	14,32	35,65	29,99	52,23
    35	7,4	20,36	24,63	25,81	36,27	36,1	52,9
    36	7,4	20,36	25,04	25,81	36,87	36,1	53,57
    37	7,4	20,36	25,44	25,81	37,45	36,1	54,21
    38	7,4	20,36	25,83	25,81	38,02	36,1	54,85
    39	7,4	20,36	26,22	25,81	38,59	36,1	55,49
    40	7,4	20,36	26,61	31,53	39,14	38,33	56,15
    41	7,4	20,36	26,98	31,53	39,68	38,33	56,83
    42	7,4	20,36	27,35	31,53	40,21	38,33	57,53
    43	7,4	20,36	27,71	31,53	40,74	38,33	58,24
    44	7,4	20,36	28,07	31,53	41,26	38,33	58,95
    45	10,04	28,21	28,42	41,26	41,77	43,54	59,66
    46	10,04	28,21	28,76	41,26	42,28	43,54	60,38
    47	10,04	28,21	29,1	41,26	42,77	43,54	61,09
    48	10,04	28,21	29,42	41,26	43,25	43,54	61,68
    49	10,04	28,21	29,74	41,26	43,7	43,54	62,26
    50	10,04	28,21	29,97	41,26	44,04	50,25	62,82
    51	10,04	28,21	30,19	41,26	44,35	50,25	63,37
    52	10,04	28,21	30,39	41,26	44,63	50,25	63,89
    53	10,04	28,21	30,56	41,26	44,88	50,25	64,4
    54	10,04	28,21	30,71	41,26	45,1	50,25	64,92
    55	12,69	30,86	30,84	45,17	45,28	53,62	65,44
    56	12,69	30,86	30,94	45,17	45,42	53,62	65,98
    57	12,69	30,86	31,01	45,17	45,52	53,62	66,53
    58	12,69	30,86	31,05	45,17	45,58	53,62	67,09
    59	12,69	30,86	31,07	45,17	45,6	53,62	67,61
    60	12,69	30,86	31,13	45,17	45,7	62,74	68,26
    61	12,69	30,86	31,18	45,17	45,76	62,74	68,87
    62	12,69	30,86	31,21	45,17	45,8	62,74	69,45
    63	12,69	30,86	31,22	45,17	45,82	62,74	70
    64	12,69	30,86	31,22	45,17	45,83	62,74	70,47
    65	12,79	30,86	31,21	45,17	45,63	65,44	70,88
    66	12,79	30,86	31,15	45,17	45,63	65,44	71,21
    67	12,79	30,86	31,07	45,17	45,63	65,44	71,46
    68	12,79	30,86	30,98	45,17	45,63	65,44	71,61
    69	12,79	30,86	30,87	45,17	45,63	65,44	71,74
    70	12,79	30,86	30,73	45,17	44,22	65,44	71,85""".split('\n')

    signaliduna = models.Company.query.filter_by(short_name='signaliduna').first()

    tarif1 = models.Tariff(
        name='ZahnBASISpur',
        company=signaliduna,
        unlimited=0,
        prosthodontics=50,
        description=''
    )
    db.session.add(tarif1)

    tarif2 = models.Tariff(
        name='ZahnPLUSpur',
        company=signaliduna,
        unlimited=0,
        prosthodontics=70,
        description=''
    )
    db.session.add(tarif2)

    tarif3 = models.Tariff(
        name='ZahnPLUS',
        company=signaliduna,
        unlimited=1,
        prosthodontics=70,
        description=''
    )
    db.session.add(tarif3)

    tarif4 = models.Tariff(
        name='ZahnTOPpur',
        company=signaliduna,
        unlimited=0,
        prosthodontics=90,
        description=''
    )
    db.session.add(tarif4)

    tarif5 = models.Tariff(
        name='ZahnTOP',
        company=signaliduna,
        unlimited=1,
        prosthodontics=90,
        description=''
    )
    db.session.add(tarif5)

    tarif6 = models.Tariff(
        name='ZahnEXKLUSIVpur',
        company=signaliduna,
        unlimited=0,
        prosthodontics=100,
        description=''
    )
    db.session.add(tarif6)

    tarif7 = models.Tariff(
        name='ZahnEXKLUSIV',
        company=signaliduna,
        unlimited=1,
        prosthodontics=100,
        description=''
    )
    db.session.add(tarif7)

    for each in table:
        a0 = each.strip().split('	')[0]
        a1 = float(each.strip().split('	')[1].replace(',', '.'))
        a2 = float(each.strip().split('	')[2].replace(',', '.'))
        a3 = float(each.strip().split('	')[3].replace(',', '.'))
        a4 = float(each.strip().split('	')[4].replace(',', '.'))
        a5 = float(each.strip().split('	')[5].replace(',', '.'))
        a6 = float(each.strip().split('	')[6].replace(',', '.'))
        a7 = float(each.strip().split('	')[7].replace(',', '.'))

        if not a3: continue
        if not a5: continue
        if not a7: continue

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

        new = models.Condition(
            tariff=tarif3,
            min_age=int(a0) if '-' not in a0 else int(a0.split('-')[0]),
            max_age=int(a0) if '-' not in a0 else int(a0.split('-')[1]),
            price=a3
        )
        db.session.add(new)

        new = models.Condition(
            tariff=tarif4,
            min_age=int(a0) if '-' not in a0 else int(a0.split('-')[0]),
            max_age=int(a0) if '-' not in a0 else int(a0.split('-')[1]),
            price=a4
        )
        db.session.add(new)

        new = models.Condition(
            tariff=tarif5,
            min_age=int(a0) if '-' not in a0 else int(a0.split('-')[0]),
            max_age=int(a0) if '-' not in a0 else int(a0.split('-')[1]),
            price=a5
        )
        db.session.add(new)

        new = models.Condition(
            tariff=tarif6,
            min_age=int(a0) if '-' not in a0 else int(a0.split('-')[0]),
            max_age=int(a0) if '-' not in a0 else int(a0.split('-')[1]),
            price=a6
        )
        db.session.add(new)

        new = models.Condition(
            tariff=tarif7,
            min_age=int(a0) if '-' not in a0 else int(a0.split('-')[0]),
            max_age=int(a0) if '-' not in a0 else int(a0.split('-')[1]),
            price=a7
        )
        db.session.add(new)

    db.session.commit()
