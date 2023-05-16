import os

from flask import render_template, send_file, request

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
        age = request.args.get('age') if request.args.get('age') else 18
        teeth = request.args.get('teeth') if request.args.get('teeth') else 0
        prosthodontics = request.args.get('prosthodontics', '')
        orto = request.args.get('orto', '')
        data = {'age': age, 'teeth': teeth, 'prosthodontics': prosthodontics, 'orto': orto}

        return render_template('results.html', **data)
