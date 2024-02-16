import time
import seeed_dht

sensor = seeed_dht.DHT("11", 12)

def get_values():
        humi, temp = sensor.read()
        return humi, temp
