#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
from setuptools import setup, find_packages

MIDDLEWARE_BASE_DIR = os.path.abspath(os.path.dirname(__file__))

meta_file = open(os.path.join(MIDDLEWARE_BASE_DIR, "django_jaeger_middleware", "metadata.py")).read()
md = dict(re.findall(r"__([a-z]+)__\s*=\s*'([^']+)'", meta_file))

with open(os.path.join(MIDDLEWARE_BASE_DIR, 'README.md')) as f:
    long_description = f.read()

setup(
    name='django-jaeger-middleware',
    license='MIT',
    version=md['version'],
    description='python(django) tracing middleware tool: django-jaeger-middleware',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=md['author'],
    author_email=md['authoremail'],
    url="https://github.com/GalphaXie/django-jaeger-middleware",
    download_url='https://github.com/GalphaXie/django-jaeger-middleware',
    packages=find_packages(),
    install_requires=[
        "jaeger_client",
        "opentracing"
    ],
    keywords=['django', 'jaeger', 'jaegertracing'],
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    zip_safe=False
)
