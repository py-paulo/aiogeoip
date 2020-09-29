import aiohttp
import ujson

from .model import Geolocation


async def get(uri):
    async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
        try:
            async with session.get(uri) as resp:
                return await resp.json()
        except aiohttp.client_exceptions.ClientOSError:
            pass    # sem conexão com a internet

        return {}


def create_obj_geolocation(dic):
    if isinstance(dic, str):
        dic = ujson.load(dic)

    if len(dic) != 19:
        return None

    return Geolocation(dic)
