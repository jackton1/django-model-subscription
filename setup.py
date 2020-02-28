"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
Autogenerated by poetry-setup:
https://github.com/orsinium/poetry-setup
"""
# IMPORTANT: this file is autogenerated. Do not edit it manually.
# All changes will be lost after `poetry-setup` command execution.
# ----------------------------------------------------------------
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open
here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.
setup(
    # https://packaging.python.org/specifications/core-metadata/#name
    name='django-model-subscription',  # Required
    # https://www.python.org/dev/peps/pep-0440/
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.9',  # Required
    # https://packaging.python.org/specifications/core-metadata/#summary
    description="Subscription model for a django model instance.",  # Required
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=long_description,  # Optional
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url="https://django-model-subscription.readthedocs.io/en/latest/index.html",  # Optional
    author="Tonye Jack",  # Optional
    author_email="tonyejck@gmail.com",  # Optional
    # For a list of valid classifiers, see https://pypi.org/classifiers/
        classifiers=['Environment :: Web Environment',
                     'Framework :: Django',
                     'Framework :: Django :: 1.11',
                     'Framework :: Django :: 2.0',
                     'Framework :: Django :: 2.1',
                     'Framework :: Django :: 2.2',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 2',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.4',
                     'Programming Language :: Python :: 3.5',
                     'Programming Language :: Python :: 3.6',
                     'Programming Language :: Python :: 3.7',
                     'Programming Language :: Python :: 3.8',
                     'Topic :: Internet :: WWW/HTTP',
                     'Topic :: Internet :: WWW/HTTP :: Dynamic Content'],  # Optional
        keywords=' '.join(['django model subscription', 'model observer', 'model change subscriber',
                           'model subscriptions', 'model instance subscription']),  # Optional
    packages=find_packages(
        exclude=[
                '__pycache__',
                '*.pyc',
                '*.pyo',
                '*.orig',
                'tests',
                'model_subscription/tests.py',
                'demo',
        ]
    ),  # Required
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
            'typing (>=3.6,<4.0); python_version >= "2.7" and python_version < "2.8" or python_version >= "3.4" and python_version < "3.5"',
            'django-lifecycle (>=0.3.0,<0.4.0)',
            'typing_extensions (>=3.7,<4.0)',
            'six (>=1.14,<2.0); python_version >= "2.0.0" and python_version < "3.0.0"',
    ],  # Optional
    # https://setuptools.readthedocs.io/en/latest/setuptools.html#dependencies-that-aren-t-in-pypi
    dependency_links=[
    ],  # Optional
    extras_require={'deploy': [], 'development': []},
    # https://stackoverflow.com/a/16576850
    include_package_data=True,
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    project_urls={  # Optional
            'homepage': 'https://django-model-subscription.readthedocs.io/en/latest/index.html',
    },
)
