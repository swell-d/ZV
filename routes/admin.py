from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user

import dbf
import models
import routes.error


def admin_routes(app):
    @app.route('/admin/users', methods=['GET'])
    @login_required
    def admin_users():
        if not current_user.admin: return routes.error.code404()
        data = {'title': f"Users", 'users': models.User.query.all()}
        return render_template('admin/users.html', **data)

    @app.route('/admin/users/<int:user_id>/delete', methods=['POST'])
    @login_required
    def admin_delete_user(user_id):
        if not current_user.admin: return routes.error.code404()
        dbf.delete_user(user_id=user_id)
        flash(f"User with id {user_id} deleted.")
        return redirect(url_for('admin_users'))
