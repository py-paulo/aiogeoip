"""The API limits the number of requests per minute, you must do the
control on your own. What we do is a basic task but does not
guarantee the correct functioning of your software.

>>> import urllib.request
>>> import socket
>>> import asyncio
>>> async def main(domains):
...     for dns in domains:
...         try:
...             ip = socket.gethostbyname(dns)
...             geo = await geoip(ip)
...         except socket.gaierror:
...             pass
>>> url_domains_example = ('https://raw.githubusercontent.com/'
...                        'py-paulo/aiogeoip/master/examples/domains.txt')
>>> with urllib.request.urlopen(url_domains_example) as response:
...     body = response.read().decode('utf-8', errors='ignore')
>>> lines = [line.lower() for line in body.split('\\n')]
>>> asyncio.get_event_loop().run_until_complete(main(lines))
"""

import asyncio
import aiohttp
import ujson
import logging

from aiogeoip.utils import create_obj_geolocation

uri_get_public_ip = 'http://meuip.com/api/meuip.php'
uribase = 'http://ip-api.com/json/'
query = '?fields=20512767'
"""
generated numeric: 20512767

generated fields:
http://ip-api.com/json/{query}?fields=status,message,continent,continentCode,
                       country,countryCode,region,regionName,city,
                       district,zip,lat,lon,timezone,isp,org,as,hosting,reverse,query
"""


async def get(uri, attempts: int, max_attempts: int, time_sleep: int) -> dict:
    """Asynchronous GET request to IP-API with JSON response

    Args:
        uri (str): complete URL
        attempts (int): number of attempts already made
        max_attempts (int): maximum attempts
        time_sleep (int): waiting time between attempts

    Returns:
        dict: raw geolocation
    """
    if attempts == max_attempts:
        return None

    async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
        try:
            async with session.get(uri) as resp:
                if resp.status == 200:
                    return await resp.json()
                elif resp.status == 429:
                    logging.debug(('the user has sent many orders in a given '
                                   'period of time. sleep two seconds.'))
                else:
                    logging.warning('abnormal response code "%s".' % resp.status)
        except aiohttp.client_exceptions.ClientOSError:
            logging.debug(('the internet connection has been interrupted '
                           'or the server is no longer available.'))
        await asyncio.sleep(time_sleep)

        return await get(uri, attempts + 1, max_attempts, time_sleep)


async def geoip(ip: str, attempts=0, max_attempts=3, time_sleep=2):
    """Geolocation object from an IP address

    Args:
        ip (str): ipv4
        attempts (int): number of attempts already made
        max_attempts (int): maximum attempts
        time_sleep (int): waiting time between attempts

    Returns:
        Geolocation or None: obj geolocation

    Example response IP-API:

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
    """

    uri = '%s%s%s' % (uribase, ip, query)

    geo = await get(uri, attempts, max_attempts, time_sleep)
    addr = create_obj_geolocation(geo)

    return addr
