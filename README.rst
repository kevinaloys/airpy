AirPy
=====

.. image:: https://travis-ci.org/kevinaloys/airpy.svg
    :target: https://travis-ci.org/kevinaloys/airpy
    
- Users can install offline versions of the Official Python Documentation
  or the documentation of their favorite Python packages.

- Can view the offline documentation through a local server instance.

- Have the ability to specify specific versions of the documentation they
  wish to install e.g Python 3.4, Django 1.7

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
        search     Search for Python docs.
        show       Show information about installed docs.
        start      Start a doc in a browser.


Start offline Documentation::

    $ airpy start django
    $ Django 1.7 docs available at http://localhost:80/django-1.7/
