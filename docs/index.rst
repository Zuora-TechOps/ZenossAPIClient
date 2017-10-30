.. ZenossAPIClient documentation master file, created by
   sphinx-quickstart on Sat Oct 21 19:45:37 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

``zenossapi`` - Zenoss API client module
========================================

`zenossapi <https://pypi.python.org/pypi?name=ZenossAPIClient&version=0.1.0&:action=display>`_ is a python module for interacting with the Zenoss API an an object-oriented way.
The philosophy here is to use objects to work with everything in the Zenoss API, and to try to normalize the various calls to the different routers.
Thus *get* methods will always return an object, *list* methods will return data.
All methods to add or create start with *add*, all remove or delete start with *delete*.
As much as possible the methods try to hide the idiosyncrasies of the JSON API, and to do the work for you, for example by letting you use a device name instead of having to provide the full device UID for every call.

.. toctree::
   :maxdepth: 3
   :caption: Contents:

   zenossapi
   zenossapi.routers



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
