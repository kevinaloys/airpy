AirPy
=====

.. image:: https://travis-ci.org/kevinaloys/airpy.svg
    :target: https://travis-ci.org/kevinaloys/airpy

Usage
-----

Installation::

    $ pip install airpy
    $ airpy
    
    Usage: airpy [OPTIONS] COMMAND [ARGS]...

        AirPy : Documentation Installer for the Pythonic Soul™

    Options:
        --help  Show this message and exit.

    Commands:
        autopilot  Auto install docs.
        install    Install offline doc of a Python module.
        list       List installed docs.
        remove     Remove an installed doc.
        start      Start a doc in a browser.


Install a Documentation::

    $ airpy install requests
    $ airpy install flask

Start the Documentation::
    
    $ airpy start requests
    $ airpy start flask

Remove a Documentation::

    $ airpy remove requests
    $ airpy remove flask

Auto Install Documentation for Python packages already installed in your system.::

    $ airpy autopilot
    $ airpy list
      sphinx  wheel  requests  pip  jinja2  setuptools 
