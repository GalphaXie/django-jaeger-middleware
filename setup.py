#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
from setuptools import setup

MIDDLEWARE_BASE_DIR = os.path.abspath(os.path.dirname(__file__))

meta_file = open(os.path.join(MIDDLEWARE_BASE_DIR, "django_jaeger_middleware", "metadata.py")).read()
md = dict(re.findall(r"__([a-z]+)__\s*=\s*'([^']+)'", meta_file))

with open(os.path.join(MIDDLEWARE_BASE_DIR, 'README.md')) as f:
    long_description = f.read()

setup(
    name='django-jaeger-middleware',
    packages=['django_jaeger_middleware'],
    license='MIT',
    version=md['version'],
    description='python(django) tracing middleware tool: django-jaeger-middleware',
    long_description=long_description,
    author=md['author'],
    author_email=md['authoremail'],
    url="https://github.com/GalphaXie/django-jaeger-middleware",
    download_url='https://github.com/GalphaXie/django-jaeger-middleware',
    install_requires=[
        "jaeger_client",
    ],
    keywords=['django', 'jaeger', 'jaegertracing'],
    classifiers=[
        "Framework :: Django"
    ],
    zip_safe=False
)
