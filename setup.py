# coding=utf-8
from setuptools import find_packages, setup

__author__ = "Gareth Coles"


setup(
    name='ultros.networks',
    version='0.0.1',
    author='Gareth Coles, Sean Gordon',
    author_email='Gareth Coles <gdude2002@gmail.com>',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='http://pypi.python.org/pypi/ultros.networks/',
    license='LICENSE.txt',
    description='Officially-supported networks for Ultros',
    long_description=open('README.txt').read(),
    install_requires=open(
        "requirements.txt"
    ).read().replace("\r", "").split("\n"),
    namespace_packages=["ultros", "ultros.networks"]
)
