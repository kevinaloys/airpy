AirPy: Documentation Installer for the Pythonic Soul
====================================================

!(https://travis-ci.org/kevinaloys/airpy.svg)

!(https://pypip.in/download/airpy/badge.svg?style=flat)

![airpy](http://i.imgur.com/8ovPxQg.png?1)

Usage
-----

Installation::

    $ pip install airpy
    
Run::

    $ airpy


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

