from flask_admin import Admin
from flask_admin.base import AdminIndexView  # noqa
from flask_admin.contrib.pymongo import ModelView  # noqa

from flask_simplelogin import login_required

# decorate Flask-Admin views via Monkey Patching
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)

# Protect model view with login
# use `from talkshow.ext.admin import LoginRequiredModelView` on blueprints
LoginRequiredModelView = ModelView
LoginRequiredModelView._handle_view = login_required(
    LoginRequiredModelView._handle_view
)


def configure(app):
    """Adds admin extension to app"""
    app.admin = Admin(
        app,
        app.config.get('FLASK_ADMIN_NAME', "Admin"),
        template_mode=app.config.get('FLASK_ADMIN_TEMPLATE_MODE', "bootstrap2")
    )
