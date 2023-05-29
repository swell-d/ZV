import models


def create(db):
    barmenia = models.Company.query.filter_by(short_name='barmenia').first()

    # tarif1 = models.Tariff(
    #     name='Mehr Zahnvorsorge',
    #     company=barmenia,
    #     unlimited=0,
    #     prosthodontics=0,
    #     orto=0,
    #     description=''
    # )
    # db.session.add(tarif1)

    tarif2 = models.Tariff(
        name='Mehr Zahnvorsorge Bonus',
        company=barmenia,
        unlimited=0,
        prosthodontics=0,
        orto=0,
        description=''
    )
    db.session.add(tarif2)

    # new = models.Condition(
    #     tariff=tarif1,
    #     min_age=0,
    #     max_age=20,
    #     price=15
    # )
    # db.session.add(new)
    #
    # new = models.Condition(
    #     tariff=tarif1,
    #     min_age=21,
    #     max_age=99,
    #     price=9
    # )
    # db.session.add(new)

    new = models.Condition(
        tariff=tarif2,
        min_age=0,
        max_age=20,
        price=15
    )
    db.session.add(new)

    new = models.Condition(
        tariff=tarif2,
        min_age=21,
        max_age=99,
        price=9
    )
    db.session.add(new)

    db.session.commit()
