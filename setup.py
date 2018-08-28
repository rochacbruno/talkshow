# coding: utf-8
from setuptools import setup, find_packages

requirements = [
    'flask',
    'pymongo',
    'tinymongo',
    'flask-simplelogin',
    'flask-admin',
    'flask-wtf',
    'flask-restful',
    'flask-bootstrap',
    'python-dotenv',
    'flasgger',
    'dynaconf'
]

requirements_extra = {
    'dev': [
        'flake8',
        'codecov',
        'pytest',
        'pytest-cov',
        'pytest-flask',
    ]
}

setup(
    name='talkshow',
    version='0.1.0',
    description="Call for papers system",
    packages=find_packages(include=['talkshow', 'talkshow.*']),
    include_package_data=True,
    install_requires=requirements,
    extras_require=requirements_extra
)
