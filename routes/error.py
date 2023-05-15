from flask import render_template


def code404():
    data = {'title': '404 Not found'}
    return render_template('errors/error.html', **data), 404


def error_routes(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return code404()
