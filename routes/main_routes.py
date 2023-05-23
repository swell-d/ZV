import os

from flask import render_template, send_file, request

import routes.error

allianz = {
    'brand': 'Allianz',
    'logo': 'allianz.svg',
    'description': 'Allianz description',
    'price': '123€ в месяц'
}
barmenia = {
    'brand': 'Barmenia',
    'logo': 'barmenia.svg',
    'description': 'Barmenia description',
    'price': '234€ в месяц'
}
diebayerische = {
    'brand': 'die Bayerische',
    'logo': 'diebayerische.svg',
    'description': 'die Bayerische description',
    'price': '345€ в месяц'
}
muenchenerverein = {
    'brand': 'Münchener Verein',
    'logo': 'muenchener-verein.svg',
    'description': 'Münchener Verein description',
    'price': '456€ в месяц'
}
signaliduna = {
    'brand': 'SIGNAL IDUNA',
    'logo': 'signal-iduna.svg',
    'description': 'SIGNAL IDUNA description',
    'price': '567€ в месяц'
}
nuernberger = {
    'brand': 'NÜRNBERGER',
    'logo': 'nuernberger.svg',
    'description': 'NÜRNBERGER description',
    'price': '678€ в месяц'
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
        age = request.args.get('age') if request.args.get('age') else 18
        teeth = request.args.get('teeth') if request.args.get('teeth') else 0
        prosthodontics = request.args.get('prosthodontics', '')
        orto = request.args.get('orto', '')

        data = {'cards': [allianz, barmenia, diebayerische, muenchenerverein, signaliduna, nuernberger]}

        return render_template('results.html', **data)
