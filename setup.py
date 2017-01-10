
"""Based on PyPA's sample project.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sidaskc',

    version='0.1',

    description='a SImple DArkSKy Client',
    long_description=long_description,

    url='https://github.com/hirnsalat/sidaskc',

    author='Alex Steiner',
    author_email='blumiger@hirnsal.at',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities',
        'Operating System :: POSIX :: Linux',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='weather darksky commandline',

    py_modules=["sidaskc"],

    install_requires=[
            "Beaker==1.8.1",
            "forecastiopy==0.21",
            "geopy==1.11.0",
            "requests==2.12.4",
            ],

    extras_require={
    },

    package_data={
    },

    entry_points={
        'console_scripts': [
            'sidaskc=sidaskc:main',
        ],
    },
)
