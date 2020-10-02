# Changelog

## 0.0.2 (02-10-2020)

### Features

* In the backend with `urllib` a deal is made with number of attempts and maximum number of attempts so that if an error occurs, such as HTTP code 429, the request is redone.

### Bugfixes

* When an error in the request with `urllib` occurred an exception was thrown, now it is just notified with` logging.debug` and returned `None`.
