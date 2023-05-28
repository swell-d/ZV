import os

from flask import render_template, send_file, request

import dbf
import routes.error

allianz = {
    'brand': 'Allianz',
    'logo': 'allianz.svg',
    'description': 'Allianz description',
    'price': 123
}
barmenia = {
    'brand': 'Barmenia',
    'logo': 'barmenia.svg',
    'description': 'Barmenia description',
    'price': 234
}
diebayerische = {
    'brand': 'die Bayerische',
    'logo': 'diebayerische.svg',
    'description': 'die Bayerische description',
    'price': 345
}
muenchenerverein = {
    'brand': 'Münchener Verein',
    'logo': 'muenchener-verein.svg',
    'description': 'Münchener Verein description',
    'price': 456
}
nuernberger = {
    'brand': 'NÜRNBERGER',
    'logo': 'nuernberger.svg',
    'description': 'NÜRNBERGER description',
    'price': 567
}
signaliduna = {
    'brand': 'SIGNAL IDUNA',
    'logo': 'signal-iduna.svg',
    'description': 'SIGNAL IDUNA description',
    'price': 678
}


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

        data = {'cards': []}

        if age >= 18 and teeth == 0 and orto == '':
            for condition in dbf.get_conditions('allianz', age):
                data['cards'].append({
                    'brand': condition.tariff.company.name,
                    'logo': condition.tariff.company.logo,
                    'tariff_name': condition.tariff.name,
                    'price': condition.price
                })
            data['cards'] += [barmenia, diebayerische, muenchenerverein, nuernberger, signaliduna]

        elif age >= 18 and teeth == 1 and orto == '':
            data['cards'] += [barmenia, diebayerische]
            for condition in dbf.get_conditions('allianz', age):
                data['cards'].append({
                    'brand': condition.tariff.company.name,
                    'logo': condition.tariff.company.logo,
                    'tariff_name': condition.tariff.name,
                    'price': round(condition.price * 1.25, 2)
                })
            data['cards'] += [muenchenerverein, nuernberger, signaliduna]

        elif age >= 18 and teeth == 2 and orto == '':
            data['cards'] += [barmenia]
            for condition in dbf.get_conditions('allianz', age):
                data['cards'].append({
                    'brand': condition.tariff.company.name,
                    'logo': condition.tariff.company.logo,
                    'tariff_name': condition.tariff.name,
                    'price': round(condition.price * 1.5, 2)
                })
            data['cards'] += [signaliduna, diebayerische, muenchenerverein, nuernberger]

        elif age >= 18 and teeth == 3 and orto == '':
            for condition in dbf.get_conditions('allianz', age):
                data['cards'].append({
                    'brand': condition.tariff.company.name,
                    'logo': condition.tariff.company.logo,
                    'tariff_name': condition.tariff.name,
                    'price': round(condition.price * 1.75, 2)
                })
            data['cards'] += [barmenia, signaliduna, diebayerische, muenchenerverein, nuernberger]

        elif age >= 18 and teeth >= 4 and orto == '':
            data['cards'] += [nuernberger]

        elif age >= 18 and orto != '':
            data = {'cards': [diebayerische, muenchenerverein]}

        elif age < 18 and orto == '':
            data = {'cards': [allianz, barmenia, diebayerische, muenchenerverein, nuernberger, signaliduna]}
        elif age < 18 and orto != '':
            data = {'cards': [allianz, signaliduna, barmenia, diebayerische, muenchenerverein, nuernberger]}

        return render_template('results.html', **data)
