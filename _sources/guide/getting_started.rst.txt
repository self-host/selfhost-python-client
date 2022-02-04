Getting Started
---------------
Assuming that you have Python 3.7 or higher and ``virtualenv`` installed, set up your environment and install the required dependencies like this:

.. code-block:: sh

    $ git clone https://github.com/self-host/selfhost-python-client.git
    $ cd selfhost-python-client
    $ virtualenv venv
    ...
    $ . venv/bin/activate
    $ python -m pip install -r requirements/requirements.txt


Using Self-host python client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
~~~~~~~~~~~~~
You can run tests in all supported Python versions using ``tox``. By default,
it will run all of the unit tests, linters and coverage. Note that this requires that you have all supported
versions of Python installed, otherwise you must pass ``-e``.

.. code-block:: sh

    $ tox
    $ tox -e py37,py38
