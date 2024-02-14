import time
from grove.grove_loudness_sensor import GroveLoudnessSensor

PIN = 0

sensor = GroveLoudnessSensor(PIN)


def get_loudness():
    return sensor.value
