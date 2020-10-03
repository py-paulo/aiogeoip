import ujson

from .model import Geolocation


def create_obj_geolocation(dic: dict) -> Geolocation or None:
    if isinstance(dic, str):
        dic = ujson.load(dic)

    if dic is None:
        return None

    if len(dic) != 19:
        return None

    return Geolocation(dic)
