from flask import current_app as app
from flask_simplelogin import SimpleLogin
from werkzeug.security import check_password_hash, generate_password_hash


def login_checker(user):
    """Valida o usuario e senha para efetuar o login"""
    username = user.get('username')
    password = user.get('password')
    if not username or not password:
        return False
    existing_user = app.db['users'].find_one({'username': username})
    if not existing_user:
        return False
    if check_password_hash(existing_user.get('password'), password):
        return True
    return False


def create_user(username, password):
    """Registra um novo usuario caso nao esteja cadastrado"""
    if app.db['users'].find_one({'username': username}):
        raise RuntimeError(f'{username} ja esta cadastrado')
    user = {'username': username,
            'password': generate_password_hash(password)}
    return app.db['users'].insert_one(user)


def configure(app):
    """Adds login control"""
    SimpleLogin(app, login_checker=login_checker)
