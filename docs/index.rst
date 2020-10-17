.. AioGeoIP documentation master file, created by
   sphinx-quickstart on Mon Sep 28 09:38:53 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===================
Welcome to AioGeoIP
===================

**AioGeoIP** is a library for geolocation by IPv4 address that uses the `IP-API <https://ip-api.com/>`_
platform completely free of charge and provides support for parallelism with *asyncio* and synchronized
methods with *Requests* and *urllib3*, in addition to additional features for optimizing your software.

Current version is |release|

.. _GitHub: https://github.com/py-paulo/aiogeoip

Key Features
============

.. caution:

   using the free service of the `IP-API <https://ip-api.com/>`_ it is only
   possible to make 45 HTTP requests per minute from an IP address.


- Support for asynchronous requests with `aiohttp <https://docs.aiohttp.org/en/stable/>`_.
- Synchronous backend in `urllib <https://urllib3.readthedocs.io/en/latest/>`_ and `requests <https://requests.readthedocs.io/en/master/>`_.
- Cached requests for greater optimization.

Library Installation
====================

.. code-block:: bash

   $ pip install aiogeoip

Getting Started
====================

aiogeoip:

.. code-block:: python

   import socket
   import asyncio
   from aiogeoip import AioGeoIP

   async def main(aio):
      ip = socket.gethostbyname('www.google.com')
      print(await aio.geoip(ip))
   
   aio = AioGeoIP()
   asyncio.get_event_loop().run_until_complete(main(aio))

OR

.. code-block:: python

   import pprint
   import socket
   import asyncio
   from aiogeoip import geoip

   async def main():
      ip = socket.gethostbyname('www.google.com')
      pprint.pprint(await geoip(ip))

   asyncio.get_event_loop().run_until_complete(main())

urllib geoip:

.. code-block:: python

   import socket
   from aiogeoip import (requests_geoip as geoip)

   ip = socket.gethostbyname('www.google.com')
   print(geoip(ip))

requests geoip:

.. code-block:: python

   import socket
   from aiogeoip import (urllib_geoip as geoip)

   ip = socket.gethostbyname('www.google.com')
   print(geoip(ip))


Response as dict:

.. code-block:: python

   { 'as': 'AS61592 FORT LINK INTERNET'
         'CORPORATIVA BRASIL LTDA'
         'EPP',
    'city': 'Camaragibe',
    'continent': 'South America',
    'continentCode': 'SA',
    'country': 'Brazil',
    'countryCode': 'BR',
    'district': '',
    'hosting': False,
    'isp': 'FORT LINK INTERNET '
        'CORPORATIVA BRASIL LTDA EPP',
    'lat': -7.9878,
    'lon': -34.9914,
    'org': 'FORT LINK INTERNET '
        'CORPORATIVA BRASIL LTDA'
        'EPP',
    'query': '45.234.102.103',
    'region': 'PE',
    'regionName': 'Pernambuco',
    'reverse': 'fort2-103.fortlink.net.br',
    'status': 'success',
    'timezone': 'America/Recife',
    'zip': '54750'}


Source code
===========

The project is hosted on GitHub_

Please feel free to file an issue on the `bug tracker
<https://github.com/py-paulo/aiogeoip/issues>`_ if you have found a bug
or have some suggestion in order to improve the library.


Dependencies
============

- Python 3.6+
- *aiohttp*
- *requests*


Contributing
============

Please read the `instructions for contributors <https://github.com/py-paulo/aiogeoip/blob/master/CONTRIBUTING.md>`_.


Authors and License
===================

The ``aiohttp`` package is written mostly by Nikolay Kim and Andrew Svetlov.

It's *Apache 2* licensed and freely available.

Feel free to improve this package and send a pull request to GitHub_.


Table Of Contents
=================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   response
   aio_usage
   sync_geoip
