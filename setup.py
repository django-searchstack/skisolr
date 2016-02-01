#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="skisolr",
    version="1.0.0b1",
    description="Lightweight python wrapper for Apache Solr.",
    author='Tadas Dailyda',
    author_email='tadas@dailyda.com',
    long_description=open('README.rst', 'r').read(),
    py_modules=[
        'pysolr'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    url='http://github.com/django-searchstack/skisolr',
    license='BSD',
    install_requires=[
        'requests>=2.0'
    ],
    tests_require=[
        'nose',
        'coverage',
    ]
)
