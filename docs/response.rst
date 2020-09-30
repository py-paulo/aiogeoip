.. currentmodule:: model

==============
Response GeoIP
==============

Regardless of the backend you use the response structure will be the
same, a ``Geolocation`` object that inherits attributes from a ``dict`` 
which means that it can be instantiated with a dictionary only, the 
attributes are read-only, in case you want to modify some field, 
you must recreate the object.

.. class:: Geolocation({\
                        'query': (str,), \
                        'continent': (str,), \
                        'continentCode': (str,), \
                        'country': (str,), \
                        'countryCode': (str,), \
                        'region': (str,), \
                        'regionName': (str,), \
                        'city': (str,), \
                        'district': (str,), \
                        'zip': (str,), \
                        'lat': (float,), \
                        'lon': (float,), \
                        'timezone': (str,), \
                        'isp': (str,), \
                        'org': (str,), \
                        'as': (str,), \
                        'reverse': (str,), \
                    })

    .. attribute:: query

        Address IPv4
    
    .. attribute:: continent

        Name to continent

