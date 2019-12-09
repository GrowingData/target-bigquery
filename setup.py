#!/usr/bin/env python

from setuptools import setup

setup(name='target-bq',
      version='1.4.0',
      description='Singer.io target for writing data to Google BigQuery',
      author='Terence Sigankais / RealSelf Business Intelligence',
      url='https://github.com/GrowingData/target-bigquery',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['target_bq'],
      install_requires=[
          'singer-python>=1.5.0',
          'google-api-python-client>=1.6.2',
          'google-cloud>=0.34.0',
          'google-cloud-bigquery>=1.9.0',
          'oauth2client',
      ],
      entry_points='''
          [console_scripts]
          target-bq=target_bq:main
      ''',
)
