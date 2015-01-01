AirPy
=====

.. image:: https://travis-ci.org/kevinaloys/airpy.svg
    :target: https://travis-ci.org/kevinaloys/airpy

At the moment, AirPy works as intended in Python 3.4, backward compatibility arriving soon for Python 3.2 and 2.7
\m/ \m/ Rock Rules!

Usage
-----

Installation::

    $ pip install airpy
    
Run::

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

Start the Documentation in a browser::
    
    $ airpy start requests

Remove a Documentation::

    $ airpy remove requests

AirPy Autopilot : Install Documentation for Python packages already installed in your system.::

    $ airpy autopilot
    $ airpy list
      flask   requests   django   sphinx   wheel   setuptools

