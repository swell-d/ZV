import os

from flask import render_template, send_file

import routes.error


def main_routes(app):
    @app.route('/', methods=['GET'])
    def home():
        data = {'title': 'Заголовок'}
        return render_template('home.html', **data)

    @app.route('/static/<path:url>', methods=['GET'])
    def route_static(url):
        if not os.path.isfile(os.path.join('static', url)):
            return routes.error.code404()
        return send_file(os.path.join('static', url))
