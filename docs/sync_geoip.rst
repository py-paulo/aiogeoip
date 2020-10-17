.. currentmodule:: aiogeoip.requests_geoip

=================
Synchronous Geoip
=================

Both backends with ``requests`` or ``urllib`` have error handling
for **connection loss** and return code **429** which means that
the user has reached the maximum number of requests per min that
is **45**. Other errors not found should be reported through 
`issues <https://github.com/py-paulo/aiogeoip/issues>`_ for us to correct.

The tests are simple so they are done with ``doctest`` and executed with 
the pipeline ``python-package.yml``.

geoip
-----

The request will be made to the API if for some reason it is not successful and the max_attempts
is more than 0 then the attempt will be made again, be aware that this can cause slowness,
to cancel this behavior you can set max_attempts to 0.

.. function:: geoip( \
                    ip: str, \
                    attempts: int = 0, \
                    max_attempts: int = 3, \
                    time_sleep:int = 2)
    
    :param str ip: The IPv4 address you want to geolocation.

    :param int attempts: Number of attempts that failed to obtain geolocation, do not use directly, it is strictly logical to control this field.

    :param int max_attempts: Maximum number of retries.

    :param int time_sleep: Waiting time between failed requests.