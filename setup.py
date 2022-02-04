import os
import re

from setuptools import setup

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')

requires = [
    'requests',
]


def get_version():
    init = open(os.path.join(ROOT, 'selfhost_client', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


setup(
    name='selfhost_client',
    version=get_version(),
    description='NODA Self Host Client API Library',
    long_description=open('README.rst').read(),
    author='NODA Intelligent Systems',
    author_email='mikael.brorsson@noda.se',
    url='https://github.com/self-host/selfhost-python-client',
    scripts=[],
    packages=['selfhost_client'],
    install_requires=requires,
    license='MIT License',
    python_requires='>= 3.7',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)
