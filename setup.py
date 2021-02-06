# -*- coding: utf-8 -*-
import os
from os.path import abspath, dirname, join, normpath

from setuptools import find_packages, setup

with open(join(dirname(__file__), "README.rst")) as readme:
    README = readme.read()

with open(join(dirname(__file__), "VERSION")) as f:
    VERSION = f.read()

install_requires = []
with open(join(dirname(abspath(__file__)), "requirements.txt")) as f:
    for line in f:
        install_requires.append(line.strip())

# allow setup.py to be run from any path
os.chdir(normpath(join(abspath(__file__), os.pardir)))
setup(
    name="edc-utils",
    version=VERSION,
    author="Erik van Widenfelt",
    author_email="ew2789@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    url="http://github.com/clinicedc/edc-model",
    license="GPL license, see LICENSE",
    description="Simple utilities for clinicedc/edc projects.",
    long_description=README,
    zip_safe=False,
    keywords="django base models fields forms admin",
    install_requires=install_requires,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.7",
    test_suite="runtests.main",
)
