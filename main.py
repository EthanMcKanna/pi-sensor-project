import time
import display, loudness, temp_humidity


while True:
	print(loudness.get_loudness())
	print(temp_humidity.get_values())
	time.sleep(0.5)
