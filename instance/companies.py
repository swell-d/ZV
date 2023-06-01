import models


def create(db):
    c1 = models.Company(
        name='Allianz',
        short_name='allianz',
        logo='allianz.svg',
        link='https://www.allianz.de/angebot/kooperation/gesundheit/zahnzusatzversicherung/rechner/#finber'
    )
    db.session.add(c1)
    c2 = models.Company(
        name='Barmenia',
        short_name='barmenia',
        logo='barmenia.svg',
        link='https://ssl.barmenia.de/online-versichern/#/zahnversicherung/Beitrag?adm=00163234&app=makler'
    )
    db.session.add(c2)
    c3 = models.Company(
        name='die Bayerische',
        short_name='diebayerische',
        logo='diebayerische.svg',
        link='https://www.diebayerische.de/online-berechnen/zahnzusatzversicherung/?m=098084'
    )
    db.session.add(c3)
    c4 = models.Company(
        name='Münchener Verein',
        short_name='muenchenerverein',
        logo='muenchener-verein.svg',
        link='https://www.muenchener-verein.de/zahnversicherung-tarifrechner/?vnr=33252&bd=29&agt=329&aktion=DZV-ZAHNGESUND'
    )
    db.session.add(c4)
    c5 = models.Company(
        name='NÜRNBERGER',
        short_name='nuernberger',
        logo='nuernberger.svg',
        link='https://www.nuernberger.de/beitragsrechner/zahnzusatz/schritt/angaben-beitragsberechnung?agNr=JTB-JSIcCRtXQFBWfLKQYQ%3D%3D#/'
    )
    db.session.add(c5)
    c6 = models.Company(
        name='SIGNAL IDUNA',
        short_name='signaliduna',
        logo='signal-iduna.svg',
        link='https://rechner.signal-iduna.de/ui/zahn?advnr=4353372&utm_medium=adp&utm_source=linkproxy&utm_campaign=linkgenerator&ref=linkproxy'
    )
    db.session.add(c6)
    db.session.commit()
