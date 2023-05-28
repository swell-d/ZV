import models


def create(db):
    c1 = models.Company(
        name='Allianz',
        short_name='allianz',
        logo='allianz.svg'
    )
    db.session.add(c1)
    c2 = models.Company(
        name='Barmenia',
        short_name='barmenia',
        logo='barmenia.svg'
    )
    db.session.add(c2)
    c3 = models.Company(
        name='die Bayerische',
        short_name='diebayerische',
        logo='diebayerische.svg'
    )
    db.session.add(c3)
    c4 = models.Company(
        name='Münchener Verein',
        short_name='muenchenerverein',
        logo='muenchener-verein.svg'
    )
    db.session.add(c4)
    c5 = models.Company(
        name='NÜRNBERGER',
        short_name='nuernberger',
        logo='nuernberger.svg'
    )
    db.session.add(c5)
    c6 = models.Company(
        name='SIGNAL IDUNA',
        short_name='signaliduna',
        logo='signal-iduna.svg'
    )
    db.session.add(c6)
    db.session.commit()
