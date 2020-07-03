#!/usr/bin/env python3

from setuptools import setup

setup(
    name="pod-lifecycle-demo",
    version="1.0",
    description="",
    packages=["demo"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ]
)
