from flask_admin import Admin
from flask_admin.base import AdminIndexView  # noqa
from flask_admin.contrib.pymongo import ModelView  # noqa

from flask_simplelogin import login_required

# decorate Flask-Admin view via Monkey Patching
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
ModelView._handle_view = login_required(ModelView._handle_view)


def configure(app):
    """Adds admin extension to app"""
    app.admin = Admin(app, "TalkShow", template_mode="bootstrap2")
