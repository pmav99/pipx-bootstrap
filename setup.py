#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

assert sys.version_info >= (3, 6, 0), "Python 3.6+ is required"

import io
import os

from setuptools import find_packages, setup, Command

DEPENDENCIES = []
EXCLUDE_FROM_PACKAGES = ["contrib", "docs", "tests*"]
CURDIR = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(CURDIR, "README.md"), "r", encoding="utf-8") as f:
    README = f.read()

setup(
    name="pipx-bootstrap",
    version="0.1.0.0",
    author="Chad Smith",
    author_email="grassfedcode@gmail.com",
    description="description",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/cs01/pipx-bootstrap",
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    keywords=[],
    scripts=[],
    entry_points={"console_scripts": ["pipx-bootstrap=pipxbootstrap.main:main"]},
    zip_safe=False,
    install_requires=DEPENDENCIES,
    python_requires=">=3.6",
    # license and classifier list:
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    license="License :: OSI Approved :: MIT License",
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
