===================
Synchronous Backend
===================

Both backends with ``requests`` or ``urllib`` have error handling
for **connection loss** and return code **429** which means that
the user has reached the maximum number of requests per min that
is **45**. Other errors not found should be reported through 
`issues <https://github.com/py-paulo/aiogeoip/issues>`_ for us to correct.

The tests are simple so they are done with ``doctest`` and executed with 
the pipeline ``python-package.yml``.
