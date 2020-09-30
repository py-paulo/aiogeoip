from .utils import get, create_obj_geolocation


uribase = 'http://ip-api.com/json/'
query = '?fields=20512767'
"""
generated numeric: 20512767

generated fields:
http://ip-api.com/json/{query}?fields=status,message,continent,continentCode,
                                      country,countryCode,region,regionName,city,
                                      district,zip,lat,lon,timezone,isp,org,as,hosting,reverse,query
"""


async def geoip(ip: str):
    """{ 'as': 'AS61592 FORT LINK INTERNET'
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

    uri = f'{uribase}{ip}{query}'

    geo = await get(uri)
    addr = create_obj_geolocation(geo)

    return addr
