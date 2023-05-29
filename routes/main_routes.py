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
        age = int(request.args.get('age')) if request.args.get('age') else 30
        teeth = int(request.args.get('teeth')) if request.args.get('teeth') else 0
        prosthodontics = request.args.get('prosthodontics', '')
        prosthodontics_full = request.args.get('prosthodontics_full', '')
        orto = request.args.get('orto', '')
        unlimited = request.args.get('unlimited', '')

        data = {'title': 'Подбор выгодной стоматологической страховки',
                'age': age,
                'teeth': teeth,
                'prosthodontics': prosthodontics,
                'prosthodontics_full': prosthodontics_full,
                'orto': orto,
                'unlimited': unlimited
                }

        return render_template('home.html', **data)

    @app.route('/calculate', methods=['GET'])
    def calculate():
        age = int(request.args.get('age')) if request.args.get('age') else 30
        teeth = int(request.args.get('teeth')) if request.args.get('teeth') else 0
        prosthodontics = request.args.get('prosthodontics', '')
        prosthodontics_full = request.args.get('prosthodontics_full', '')
        orto = request.args.get('orto', '')
        unlimited = request.args.get('unlimited', '')

        data = {'cards1': [], 'cards2': [], 'cards3': []}

        allianz = get_allianz(age, teeth, prosthodontics, prosthodontics_full, orto, unlimited)
        barmenia = get_barmenia(age, teeth, prosthodontics, prosthodontics_full, orto, unlimited)
        diebayerische = get_diebayerische(age, teeth, prosthodontics, prosthodontics_full, orto, unlimited)
        muenchenerverein = get_muenchenerverein(age, teeth, prosthodontics, prosthodontics_full, orto, unlimited)
        nuernberger = get_nuernberger(age, teeth, prosthodontics, prosthodontics_full, orto, unlimited)
        signaliduna = get_signaliduna(age, teeth, prosthodontics, prosthodontics_full, orto, unlimited)


        if 0 <= age < 18:
            if not orto:
                data['cards1'] += [*allianz, *barmenia]
                data['cards2'] += [*diebayerische, *muenchenerverein, *nuernberger, *signaliduna]

            elif orto:
                data['cards1'] += [*allianz, *signaliduna]
                data['cards2'] += [*barmenia, *diebayerische, *muenchenerverein, *nuernberger]

        elif 18 <= age <= 99:
            if not orto:
                if not prosthodontics:
                    data['cards1'] += [barmenia[0]] if len(barmenia) else []
                    data['cards2'] += [*allianz, *diebayerische, *muenchenerverein, *nuernberger, *signaliduna]

                elif teeth == 0:
                    data['cards1'] += [*allianz, *barmenia]
                    data['cards2'] += [*diebayerische, *muenchenerverein, *nuernberger, *signaliduna]

                elif teeth == 1:
                    data['cards1'] += [*barmenia, *diebayerische, *allianz]
                    data['cards2'] += [*muenchenerverein, *nuernberger, *signaliduna]

                elif teeth == 2:
                    data['cards1'] += [*barmenia, *allianz, *signaliduna]
                    data['cards2'] += [*diebayerische, *muenchenerverein, *nuernberger]

                elif teeth == 3:
                    data['cards1'] += [*allianz, *barmenia, *signaliduna]
                    data['cards2'] += [*diebayerische, *muenchenerverein, *nuernberger]

                elif teeth >= 4:
                    data['cards1'] += [*nuernberger]
                    data['cards3'] += [*allianz, *barmenia, *diebayerische, *muenchenerverein, *signaliduna]

            elif orto:
                data['cards1'] += [*diebayerische, *muenchenerverein]
                data['cards3'] += [*allianz, *barmenia, *nuernberger, *signaliduna]

        return render_template('results.html', **data)


def get_allianz(age, teeth, prosthodontics, prosthodontics_full, orto, unlimited):
    result = []

    if teeth == 0:
        price_increase = 1.0
    elif teeth == 1:
        price_increase = 1.25
    elif teeth == 2:
        price_increase = 1.5
    elif teeth >= 3:
        price_increase = 1.75

    for condition in dbf.get_conditions('allianz', age, teeth, prosthodontics, prosthodontics_full, orto, unlimited):
        result.append({
            'brand': condition.tariff.company.name,
            'logo': condition.tariff.company.logo,
            'tariff_name': condition.tariff.name,
            'price': round(condition.price * price_increase, 2)
        })
    return result


def get_barmenia(age, teeth, prosthodontics, prosthodontics_full, orto, unlimited):
    result = []

    for condition in dbf.get_conditions('barmenia', age, teeth, prosthodontics, prosthodontics_full, orto, unlimited):
        result.append({
            'brand': condition.tariff.company.name,
            'logo': condition.tariff.company.logo,
            'tariff_name': condition.tariff.name,
            'price': condition.price
        })
    return result


def get_diebayerische(age, teeth, prosthodontics, prosthodontics_full, orto, unlimited):
    result = []

    for condition in dbf.get_conditions('diebayerische', age, teeth, prosthodontics, prosthodontics_full, orto,
                                        unlimited):
        result.append({
            'brand': condition.tariff.company.name,
            'logo': condition.tariff.company.logo,
            'tariff_name': condition.tariff.name,
            'price': condition.price
        })
    return result


def get_muenchenerverein(age, teeth, prosthodontics, prosthodontics_full, orto, unlimited):
    result = []

    for condition in dbf.get_conditions('muenchenerverein', age, teeth, prosthodontics, prosthodontics_full, orto,
                                        unlimited):
        result.append({
            'brand': condition.tariff.company.name,
            'logo': condition.tariff.company.logo,
            'tariff_name': condition.tariff.name,
            'price': condition.price
        })
    return result


def get_nuernberger(age, teeth, prosthodontics, prosthodontics_full, orto, unlimited):
    return [{
        'brand': 'NÜRNBERGER',
        'logo': 'nuernberger.svg',
        'tariff_name': 'Platzhalter',
        'price': 999
    }]


def get_signaliduna(age, teeth, prosthodontics, prosthodontics_full, orto, unlimited):
    result = []

    for condition in dbf.get_conditions('signaliduna', age, teeth, prosthodontics, prosthodontics_full, orto,
                                        unlimited):
        result.append({
            'brand': condition.tariff.company.name,
            'logo': condition.tariff.company.logo,
            'tariff_name': condition.tariff.name,
            'price': condition.price
        })
    return result
