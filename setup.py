#!/usr/bin/env python


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import SatNOGS
version = SatNOGS.__version__

setup(
    name='SatNOGS',
    version=version,
    author='',
    author_email='info@satnogs.org',
    packages=[
        'SatNOGS',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['SatNOGS/manage.py'],
)
