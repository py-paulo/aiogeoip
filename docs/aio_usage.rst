.. currentmodule:: aiogeoip

=========
Aio Usage
=========

AioGeoIP implements the functionality of storing requests already made in a ``set`` object so
that it is not necessary to waste computer and network resources making the same request
made previously, in addition to containing methods to obtain a history of the last 100 records.

Tutorial
--------

You can use the function ``geoip`` by the class ``AioGeoIP (). Geoip`` or directly with import ``from aiogeoip import geoip``.


AioGeoIP
--------

Class for optimizing the use of Geolocation by IP

.. class:: AioGeoIP()

    .. attribute:: cache

        It is a class that stores the last 100 ``Geolocation`` objects so that no more than one request is made to the same IP address.
    
    .. method:: geoip(ip: str)

        returns a Geolocation object from the IPv4 address.

        :param str ip: IPv4 address.

    .. method:: geoips_in_cache()

        returns all stored ``Geolocation`` objects.
