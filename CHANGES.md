# Changelog

## 0.0.2 (02-10-2020)

### Features

* If a request is not successful (*return code 200*) it will be
tried again by ``N`` set by default to ``3`` in a time interval
in seconds ``N`` by default ``2 ``.
You can still call the ``geoip`` function only with a mandatory
IPv4 argument, so it will have the default behavior of trying 3 times.

### Bugfixes

* All backends deal with the *connection error* and return code **429** error.

### Improved Documentation

* Creation of the page to document the synchronous functions.

### Misc

* Basic tests for ``geoip`` function on all backends

## 0.0.3 (14-10-2020)

### Bugfixes

* **#2** ``ModuleNotFoundError: No module named 'ujson'``

## 0.0.4 (17-10-2020)

### Features

* [#3](https://github.com/py-paulo/aiogeoip/issues/3) function that returns the external IP address, private IP and hostname.

### Misc

* [#4](https://github.com/py-paulo/aiogeoip/issues/3) Support to python3.4+

### Improved Documentation

Function ``geoip`` in aio, requests and urllib background. Improved documentation for the Geolocation class.