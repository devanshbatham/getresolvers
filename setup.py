import io
from os import path
from setuptools import find_packages, setup

pwd = path.abspath(path.dirname(__file__))
with io.open(path.join(pwd, 'README.md'), encoding='utf-8') as readme:
    desc = readme.read()

setup(
    name='getresolvers',
    version=1.0,
    description='A simple utility to fetch freshly updated DNS resolvers',
    long_description=desc,
    long_description_content_type='text/markdown',
    author='Devansh Batham <devanshbatham009@gmail.com>',
    license='MIT License',
    packages=find_packages(),
    classifiers=[
        'Topic :: DNS, Resolvers, Nameservers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'getresolvers = getresolvers.getresolvers:main'
        ]
    },
    keywords=['getresolvers']
)