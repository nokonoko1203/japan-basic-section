from enum import Enum


class SystemNumber(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    SIXTH = 6
    SEVENTH = 7
    EIGHTH = 8
    NINTH = 9
    TENTH = 10
    ELEVENTH = 11
    TWELFTH = 12
    THIRTEENTH = 13
    FOURTEENTH = 14
    FIFTEENTH = 15
    SIXTEENTH = 16
    SEVENTEENTH = 17
    EIGHTEENTH = 18
    NINETEENTH = 19


class OriginCoords(Enum):
    FIRST = (129.5, 33.0)
    SECOND = (131.0, 33.0)
    THIRD = (132.166667, 36.0)
    FOURTH = (133.5, 33.0)
    FIFTH = (134.333333, 36.0)
    SIXTH = (136.0, 36.0)
    SEVENTH = (137.166667, 36.0)
    EIGHTH = (138.5, 36.0)
    NINTH = (139.5, 36.0)
    TENTH = (140.5, 40.0)
    ELEVENTH = (140.25, 44.0)
    TWELFTH = (142.25, 44.0)
    THIRTEENTH = (144.25, 44.0)
    FOURTEENTH = (142.0, 26.0)
    FIFTEENTH = (127.5, 26.0)
    SIXTEENTH = (124, 26.0)
    SEVENTEENTH = (131.0, 26.0)
    EIGHTEENTH = (136.0, 20.0)
    NINETEENTH = (154.0, 26.0)


class EpsgCode(Enum):
    FIRST = {
        "JGD2000": "EPSG:2443",
        "JGD2011": "EPSG:6669",
    }
    SECOND = {
        "JGD2000": "EPSG:2444",
        "JGD2011": "EPSG:6670",
    }
    THIRD = {
        "JGD2000": "EPSG:2445",
        "JGD2011": "EPSG:6671",
    }
    FOURTH = {
        "JGD2000": "EPSG:2446",
        "JGD2011": "EPSG:6672",
    }
    FIFTH = {
        "JGD2000": "EPSG:2447",
        "JGD2011": "EPSG:6673",
    }
    SIXTH = {
        "JGD2000": "EPSG:2448",
        "JGD2011": "EPSG:6674",
    }
    SEVENTH = {
        "JGD2000": "EPSG:2449",
        "JGD2011": "EPSG:6675",
    }
    EIGHTH = {
        "JGD2000": "EPSG:2450",
        "JGD2011": "EPSG:6676",
    }
    NINTH = {
        "JGD2000": "EPSG:2451",
        "JGD2011": "EPSG:6677",
    }
    TENTH = {
        "JGD2000": "EPSG:2452",
        "JGD2011": "EPSG:6678",
    }
    ELEVENTH = {
        "JGD2000": "EPSG:2453",
        "JGD2011": "EPSG:6679",
    }
    TWELFTH = {
        "JGD2000": "EPSG:2454",
        "JGD2011": "EPSG:6680",
    }
    THIRTEENTH = {
        "JGD2000": "EPSG:2455",
        "JGD2011": "EPSG:6681",
    }
    FOURTEENTH = {
        "JGD2000": "EPSG:2456",
        "JGD2011": "EPSG:6682",
    }
    FIFTEENTH = {
        "JGD2000": "EPSG:2457",
        "JGD2011": "EPSG:6683",
    }
    SIXTEENTH = {
        "JGD2000": "EPSG:2458",
        "JGD2011": "EPSG:6684",
    }
    SEVENTEENTH = {
        "JGD2000": "EPSG:2459",
        "JGD2011": "EPSG:6685",
    }
    EIGHTEENTH = {
        "JGD2000": "EPSG:2460",
        "JGD2011": "EPSG:6686",
    }
    NINETEENTH = {
        "JGD2000": "EPSG:2461",
        "JGD2011": "EPSG:6687",
    }


def get_coord_info(system_number: int) -> tuple:
    system_name = SystemNumber(system_number).name
    origin_coords = OriginCoords[system_name].value
    epsg_code = EpsgCode[system_name].value
    return origin_coords, epsg_code
