# coding: utf-8

from setuptools import setup

requirements = [
    'flask',
    'pymongo',
    'tinymongo',
    'flask-simplelogin',
    'flask-admin',
    'flask-wtf',
    'flask-restful',
    'flask-pytest',
    'flask-bootstrap',
    'python-dotenv',
    'flasgger'
]


setup(
    name='talkshow',
    version='0.0.1',
    description="Call for papers system",
    packages=['talkshow'],
    include_package_data=True,
    install_requires=requirements
)
