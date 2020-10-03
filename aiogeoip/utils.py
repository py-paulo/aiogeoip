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


def create_obj_geolocation(dic: dict) -> Geolocation or None:
    if isinstance(dic, str):
        dic = ujson.load(dic)

    if dic is None:
        return None

    if len(dic) != 19:
        return None

    return Geolocation(dic)
