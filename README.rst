=======================
Self-Host Python Client
=======================
|forthebadge made-with-python|

.. |forthebadge made-with-python| image:: http://ForTheBadge.com/images/badges/made-with-python.svg
   :target: https://www.python.org/

NODA Self-host client API Library.

About
=====
NODA Self-host python client is a simple, yet efficient library to interface with the NODA HTTP API exposed through NODA Self-host.

You can find the latest, most up to date, documentation at our `doc site <https://self-host.github.io/selfhost-python-client/>`_.

Getting Started
===============
Assuming that you have Python 3.7 or higher and ``virtualenv`` installed, set up your environment and install the required dependencies like this:

.. code-block:: sh

    $ git clone https://github.com/self-host/selfhost-python-client.git
    $ cd selfhost-python-client
    $ virtualenv venv
    ...
    $ . venv/bin/activate
    $ python -m pip install -r requirements/requirements.txt


Using Self-host python client
=============================
After installing self-host python client, auth credentials can be setup by either providing the credentials as input parameters to the
client in code or by exporting specific environment variables.

.. code-block:: bash

    $ export SELF_HOST_BASE_URL="my-base-url"
    $ export SELF_HOST_USERNAME="my-username"
    $ export SELF_HOST_PASSWORD="my-password"

Then, from a Python interpreter (Input parameters can be omitted if above step is used):

.. code-block:: python

    >>> from selfhost_client import SelfHostClient
    >>> client = SelfHostClient(base_url='my-base-url', username='my-username', password='my-password')
    >>> users = client.get_users()

Running Tests
=============
You can run tests in all supported Python versions using ``tox``. By default,
it will run all of the unit tests, linters and coverage. Note that this requires that you have all supported
versions of Python installed, otherwise you must pass ``-e``.

.. code-block:: sh

    $ tox
    $ tox -e py37,py38

Requirements
============

Dependencies
------------

`requests <https://github.com/psf/requests>`_

Install requirements
--------------------------------
Required dependencies:

    pip install -r requirements/requirements.txt

Dev dependencies:

    pip install -r requirements/dev.txt

Update requirements
-------------------
If a dependency is to be added to the project, add it to the appropriate .in file and run:

    pip-compile requirements/path-to-file.in

Sync local virtual environment with requirements
------------------------------------------------
If you would like to sync your local virtual environment with the generated and locked requirements of the project, run:

    pip-sync requirements/path-to-file.in requirements/another-file.in

Test suite
==========

Run test suite locally
----------------------
Navigate to the root of the project and run:

    tox

Show list of commands
---------------------
Show the list of tox commands available to run individually:

    tox -a

Run tests
---------
    tox -e py37,py38,py39,py310

Run linters
-----------
    tox -e lint

Run Coverage
------------
    tox -e cov

Build the project
-----------------
    tox -e build

Publish the project
-------------------
Must have built the project prior to running this command.

Running the following command will by default publish the build to TestPyPi:

    tox -e publish

If you want to release it to be publically accessible in PyPi, use:

    tox -e publish -- --repository pypi

Pre-commit hooks
================

It is recommended that every developer working on this project activate pre-commit hooks.

Activate pre-commit hooks
-------------------------
    pre-commit install

Documentation
=============

Build documentation
-------------------
    tox -e build-docs

This will create a docs/_build/html folder with an index.html file that can be opened in a browser.
