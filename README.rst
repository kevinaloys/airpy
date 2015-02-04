AirPy: Documentation Installer for the Pythonic Soul
====================================================

.. image:: https://travis-ci.org/kevinaloys/airpy.svg

.. image:: https://pypip.in/download/airpy/badge.svg?style=flat

Usage
-----

Installation::

    $ pip install airpy
    
Run::

    $ airpy
    
.. image:: http://imgur.com/8ovPxQg

    Usage: airpy [OPTIONS] COMMAND [ARGS]...

        AirPy : Documentation Installer for the Python

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

Start the Documentation in a browser::
    
    $ airpy start requests

Remove a Documentation::

    $ airpy remove requests

AirPy Autopilot : Install Documentation for Python packages already installed in your system.::

    $ airpy autopilot
    $ airpy list
      flask   requests   django   sphinx   wheel   setuptools

