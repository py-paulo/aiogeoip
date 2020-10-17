.. currentmodule:: aiogeoip.model

=====================
Geolocation Reference
=====================

Geolocation Response object
---------------------------

Regardless of the backend you use the response structure will be the
same, a ``Geolocation`` object that inherits attributes from a ``dict`` 
which means that it can be instantiated with a dictionary only, the 
attributes are read-only, in case you want to modify some field, 
you must recreate the object.

You will not normally need to interact directly with this class,
since the object is created automatically by the main function,
independent from the backend, for this reason no attributes were created
private and setters.

.. class:: Geolocation({ \
                        query: str, \
                        continent: str, \
                        continentCode: str, \
                        country: str, \
                        countryCode: str, \
                        region: str, \
                        regionName: str, \
                        city: str, \
                        district: str, \
                        zip: str, \
                        lat: float, \
                        lon: float, \
                        timezone: str, \
                        isp: str, \
                        org: str, \
                        as: str, \
                        reverse: str, \
                    })
    
    .. attribute:: location

        Is the junction of latitude and longitude: ``lat, location``.
    
    .. attribute:: address

        Full name of the IP address: ``continent, country, region_name, city``.

    .. attribute:: ip

        Address IPv4 it's equivalent to **query**
        in *dict* constructor.
    
    .. attribute:: continent

        It is the same as the "continent" field in the json response

    .. attribute:: continent_code

        It is the same as the "continentCode" field in the json response

    .. attribute:: country

        It is the same as the "country" field in the json response

    .. attribute:: country_code

        It is the same as the "countryCode" field in the json response

    .. attribute:: region

        It is the same as the "region" field in the json response

    .. attribute:: region_name

        It is the same as the "region_name" field in the json response

    .. attribute:: city

        It is the same as the "city" field in the json response

    .. attribute:: district

        It is the same as the "district" field in the json response

    .. attribute:: zip

        It is the same as the "zip" field in the json response

    .. attribute:: lat

        It is the same as the "lat" field in the json response

    .. attribute:: lon

        It is the same as the "" field in the json response

    .. attribute:: timezone

        It is the same as the "" field in the json response

    .. attribute:: isp

        It is the same as the "" field in the json response

    .. attribute:: org

        It is the same as the "" field in the json response

    .. attribute:: reverse    

        It is the same as the "" field in the json response.
