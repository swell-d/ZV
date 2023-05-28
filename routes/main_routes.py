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

        data = {'cards1': [], 'cards2': [], 'cards3': []}

        if age >= 18 and teeth == 0 and not orto:
            for condition in dbf.get_conditions('allianz', age):
                data['cards1'].append({
                    'brand': condition.tariff.company.name,
                    'logo': condition.tariff.company.logo,
                    'tariff_name': condition.tariff.name,
                    'price': condition.price
                })
            data['cards1'] += [barmenia]
            data['cards2'] += [diebayerische, muenchenerverein, nuernberger, signaliduna]

        elif age >= 18 and teeth == 1 and not orto:
            data['cards1'] += [barmenia, diebayerische]
            for condition in dbf.get_conditions('allianz', age):
                data['cards1'].append({
                    'brand': condition.tariff.company.name,
                    'logo': condition.tariff.company.logo,
                    'tariff_name': condition.tariff.name,
                    'price': round(condition.price * 1.25, 2)
                })
            data['cards2'] += [muenchenerverein, nuernberger, signaliduna]

        elif age >= 18 and teeth == 2 and not orto:
            data['cards1'] += [barmenia]
            for condition in dbf.get_conditions('allianz', age):
                data['cards1'].append({
                    'brand': condition.tariff.company.name,
                    'logo': condition.tariff.company.logo,
                    'tariff_name': condition.tariff.name,
                    'price': round(condition.price * 1.5, 2)
                })
            data['cards1'] += [signaliduna]
            data['cards2'] += [diebayerische, muenchenerverein, nuernberger]

        elif age >= 18 and teeth == 3 and not orto:
            for condition in dbf.get_conditions('allianz', age):
                data['cards1'].append({
                    'brand': condition.tariff.company.name,
                    'logo': condition.tariff.company.logo,
                    'tariff_name': condition.tariff.name,
                    'price': round(condition.price * 1.75, 2)
                })
            data['cards1'] += [barmenia, signaliduna]
            data['cards2'] += [diebayerische, muenchenerverein, nuernberger]

        elif age >= 18 and teeth >= 4 and not orto:
            data['cards1'] += [nuernberger]
            
            for condition in dbf.get_conditions('allianz', age):
                data['cards3'].append({
                    'brand': condition.tariff.company.name,
                    'logo': condition.tariff.company.logo,
                    'tariff_name': condition.tariff.name,
                    'price': round(condition.price * 1.75, 2)
                })
            data['cards3'] += [barmenia, diebayerische, muenchenerverein, signaliduna]

        elif age >= 18 and orto:
            data = {'cards1': [diebayerische, muenchenerverein]}

        elif age < 18 and not orto:
            data = {'cards1': [allianz, barmenia, diebayerische, muenchenerverein, nuernberger, signaliduna]}
        elif age < 18 and orto:
            data = {'cards1': [allianz, signaliduna, barmenia, diebayerische, muenchenerverein, nuernberger]}

        return render_template('results.html', **data)
