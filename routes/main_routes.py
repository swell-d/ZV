import os

from flask import render_template, send_file, request

import dbf
import routes.error


def main_routes(app):
    @app.route('/static/<path:url>', methods=['GET'])
    def route_static(url):
        if not os.path.isfile(os.path.join('static', url)):
            return routes.error.code404()
        return send_file(os.path.join('static', url))

    @app.route('/', methods=['GET'])
    def home():
        age = request.args.get('age') if request.args.get('age') else 18
        teeth = request.args.get('teeth') if request.args.get('teeth') else 0
        prosthodontics = request.args.get('prosthodontics', '')
        orto = request.args.get('orto', '')

        data = {'title': 'Заголовок', 'age': age, 'teeth': teeth, 'prosthodontics': prosthodontics, 'orto': orto}

        return render_template('home.html', **data)

    @app.route('/calculate', methods=['GET'])
    def calculate():
        age = int(request.args.get('age')) if request.args.get('age') else 18
        teeth = int(request.args.get('teeth')) if request.args.get('teeth') else 0
        prosthodontics = request.args.get('prosthodontics', '')
        orto = request.args.get('orto', '')

        data = {'cards1': [], 'cards2': [], 'cards3': []}

        allianz = get_allianz(age, teeth, prosthodontics, orto)
        barmenia = get_barmenia(age, teeth, prosthodontics, orto)
        diebayerische = get_diebayerische(age, teeth, prosthodontics, orto)
        muenchenerverein = get_muenchenerverein(age, teeth, prosthodontics, orto)
        nuernberger = get_nuernberger(age, teeth, prosthodontics, orto)
        signaliduna = get_signaliduna(age, teeth, prosthodontics, orto)

        if age >= 18 and teeth == 0 and not orto:
            data['cards1'] += [*allianz, *barmenia]
            data['cards2'] += [*diebayerische, *muenchenerverein, *nuernberger, *signaliduna]

        elif age >= 18 and teeth == 1 and not orto:
            data['cards1'] += [*barmenia, *diebayerische, *allianz]
            data['cards2'] += [*muenchenerverein, *nuernberger, *signaliduna]

        elif age >= 18 and teeth == 2 and not orto:
            data['cards1'] += [*barmenia, *allianz, *signaliduna]
            data['cards2'] += [*diebayerische, *muenchenerverein, *nuernberger]

        elif age >= 18 and teeth == 3 and not orto:
            data['cards1'] += [*allianz, *barmenia, *signaliduna]
            data['cards2'] += [*diebayerische, *muenchenerverein, *nuernberger]

        elif age >= 18 and teeth >= 4 and not orto:
            data['cards1'] += [*nuernberger]
            data['cards3'] += [*allianz, *barmenia, *diebayerische, *muenchenerverein, *signaliduna]

        elif age >= 18 and orto:
            data['cards1'] += [*diebayerische, *muenchenerverein]
            data['cards3'] += [*allianz, *barmenia, *nuernberger, *signaliduna]

        elif age < 18 and not orto:
            data['cards1'] += [*allianz, *barmenia, *diebayerische, *muenchenerverein, *nuernberger, *signaliduna]

        elif age < 18 and orto:
            data['cards1'] += [*allianz, *signaliduna, *barmenia, *diebayerische, *muenchenerverein, *nuernberger]

        return render_template('results.html', **data)


def get_allianz(age, teeth, prosthodontics, orto):
    result = []

    if teeth == 0:
        price_increase = 1.0
    elif teeth == 1:
        price_increase = 1.25
    elif teeth == 2:
        price_increase = 1.5
    elif teeth == 3:
        price_increase = 1.75
    else:
        price_increase = 1.75

    for condition in dbf.get_conditions('allianz', age):
        result.append({
            'brand': condition.tariff.company.name,
            'logo': condition.tariff.company.logo,
            'tariff_name': condition.tariff.name,
            'price': round(condition.price * price_increase, 2)
        })
    return result


def get_barmenia(age, teeth, prosthodontics, orto):
    return [{
        'brand': 'Barmenia',
        'logo': 'barmenia.svg',
        'tariff_name': 'Barmenia description',
        'price': 234
    }]


def get_diebayerische(age, teeth, prosthodontics, orto):
    return [{
        'brand': 'die Bayerische',
        'logo': 'diebayerische.svg',
        'tariff_name': 'die Bayerische description',
        'price': 345
    }]


def get_muenchenerverein(age, teeth, prosthodontics, orto):
    return [{
        'brand': 'Münchener Verein',
        'logo': 'muenchener-verein.svg',
        'tariff_name': 'Münchener Verein description',
        'price': 456
    }]


def get_nuernberger(age, teeth, prosthodontics, orto):
    return [{
        'brand': 'NÜRNBERGER',
        'logo': 'nuernberger.svg',
        'tariff_name': 'NÜRNBERGER description',
        'price': 567
    }]


def get_signaliduna(age, teeth, prosthodontics, orto):
    return [{
        'brand': 'SIGNAL IDUNA',
        'logo': 'signal-iduna.svg',
        'tariff_name': 'SIGNAL IDUNA description',
        'price': 678
    }]
