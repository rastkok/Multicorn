#!/usr/bin/env python

# Public Domain

from setuptools import setup, find_packages


setup(
    name = "Dyko",
    version = "0.2.dev1",
    packages = find_packages(
        exclude=["*._test", "*._test.*", "test.*", "test"]),
    package_dir = {
        "kalamar": "kalamar",
        "kraken": "kraken"},
    package_data = {
        "": ["AUTHORS"],
        "kalamar": ["access_point/xml/xml2rst.xsl"]},
    install_requires = [
        "werkzeug>=0.5"],
    extras_require = {
        "docutils": ["docutils>=0.6"],
        "lxml": ["lxml>=2.0"],
        "Genshi": ["genshi>=0.5"],
        "Mako": ["mako>=0.3"],
        "SQLAlchemy": ["sqlalchemy>=0.6"],
        "Jinja2": ["jinja2>=2.0"]},
    author = "Kozea",
    author_email = "guillaume.ayoub@kozea.fr",
    description = "This is a light and flexible web framework in full python.",
    license = "GPL",
    keywords = "web framework database",
    url = "http://www.dyko.org/",
    zip_safe=False)
