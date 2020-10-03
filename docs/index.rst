.. AioGeoIP documentation master file, created by
   sphinx-quickstart on Mon Sep 28 09:38:53 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===================
Welcome to AioGeoIP
===================

Real asynchronous geolocation by IP address with asyncio support.

Current version is |release|.

.. _GitHub: https://github.com/py-paulo/aiogeoip

Key Features
============

.. caution:

   using the free service of the `IP-API <https://ip-api.com/>`_ it is only possible to make 45 HTTP requests per minute from an IP address.


- Support for asynchronous requests with `aiohttp <https://docs.aiohttp.org/en/stable/>`_.
- Synchronous backend in ``urllib`` and ``requests``.
- Synchronous backend in urllib and requests.

Library Installation
====================

.. code-block:: bash

   $ pip install aiogeoip

If in case you wanted to use the synchronous library with ``requests``, just install it:

.. code-block:: bash

   $ pip install requests


Getting Started
====================

Aio geoip:

.. code-block:: python

   import socket
   import asyncio
   from aiogeoip import AioGeoIP

   async def main(aio):
      ip = socket.gethostbyname('www.google.com')
      print(await aio.geoip(ip))
   
   aio = AioGeoIP()
   asyncio.get_event_loop().run_until_complete(main(aio))

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


Source code
===========

The project is hosted on GitHub_

Please feel free to file an issue on the `bug tracker
<https://github.com/py-paulo/aiogeoip/issues>`_ if you have found a bug
or have some suggestion in order to improve the library.


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
   sync_backend
