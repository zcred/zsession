#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

requirements = []
test_requirements = []

setup(
    name="zsession",
    version="0.0.0",
    description="Session tokens based on the zcred credential format",
    long_description="Lightweight implementation of zcreds providing advanced session tokens",
    author="Tony Arcieri",
    author_email="bascule@gmail.com",
    url="https://github.com/zcred/zsession",
    packages=["zsession"],
    package_dir={"zsession": "zsession"},
    include_package_data=True,
    install_requires=[],
    license="MIT license",
    zip_safe=False,
    keywords=["authentication", "cryptography", "security", "serialization", "merkle"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
    ],
    test_suite="tests",
    tests_require=[]
)
