import models


def start(db):
    c1 = models.Company(
        name='Allianz',
        short_name='allianz',
        logo='allianz.svg',
        short_description='Allianz description'
    )
    db.session.add(c1)
    c2 = models.Company(
        name='Barmenia',
        short_name='barmenia',
        logo='barmenia.svg',
        short_description='Barmenia description'
    )
    db.session.add(c2)
    c3 = models.Company(
        name='die Bayerische',
        short_name='diebayerische',
        logo='diebayerische.svg',
        short_description='die Bayerische description'
    )
    db.session.add(c3)
    c4 = models.Company(
        name='Münchener Verein',
        short_name='muenchenerverein',
        logo='muenchener-verein.svg',
        short_description='Münchener Verein description'
    )
    db.session.add(c4)
    c5 = models.Company(
        name='NÜRNBERGER',
        short_name='nuernberger',
        logo='nuernberger.svg',
        short_description='NÜRNBERGER description'
    )
    db.session.add(c5)
    c6 = models.Company(
        name='SIGNAL IDUNA',
        short_name='signaliduna',
        logo='signal-iduna.svg',
        short_description='SIGNAL IDUNA description'
    )
    db.session.add(c6)
    db.session.commit()
