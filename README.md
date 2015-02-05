AirPy: Documentation Installer for the Python
=============================================

![](https://travis-ci.org/kevinaloys/airpy.svg)

![](https://pypip.in/download/airpy/badge.svg?style=flat)



Usage
-----

Installation::

    $ pip install airpy
    
Run::

    $ airpy

    Usage: airpy [OPTIONS] COMMAND [ARGS]...


    Options:
        --help  Show this message and exit.

    Commands:
        autopilot  Auto install docs.
        install    Install offline doc of a Python module.
        list       List installed docs.
        remove     Remove an installed doc.
        start      Start a doc in a browser.


![airpy](http://i.imgur.com/8ovPxQg.png)

Install a Documentation::

    $ airpy install requests

Start the Documentation in a browser
    
    $ airpy start requests

Remove a Documentation::

    $ airpy remove requests

AirPy Autopilot : Install Documentation for Python packages already installed in your system.

    $ airpy autopilot

List Installed Documentation

    $ airpy list

![airpy list](http://i.imgur.com/8VHRkeK.png)
