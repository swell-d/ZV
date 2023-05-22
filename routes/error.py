from flask import render_template


def code403():
    data = {'title': '403 Forbidden',
            'error': "Sorry, you don't have permission to access this page."}
    return render_template('errors/error.html', **data), 403


def code404():
    data = {'title': '404 Not found'}
    return render_template('errors/error.html', **data), 404


def code405():
    data = {'title': '405 Method Not Allowed',
            'error': "The method is not allowed for the requested URL."}
    return render_template('errors/error.html', **data), 405


def error_routes(app):
    @app.errorhandler(403)
    def forbidden(e):
        return code403()

    @app.errorhandler(404)
    def page_not_found(e):
        return code404()

    @app.errorhandler(405)
    def method_not_allowed(e):
        return code405()
