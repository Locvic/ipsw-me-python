# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from setuptools import find_packages, setup

setup(
    name = "ipsw-me",
    version = "1.0.0",
    license = "MIT",
    author = "Vislate",
    description = "Simple & lightweight IPSW.me API wrapper written in Python",
    url = "https://github.com/Vislate/ipsw-me-python",
    packages = find_packages(),
    python_requires = ">=3",
    install_requires = open("requirements.txt", "r", encoding="UTF8").readlines(),
)