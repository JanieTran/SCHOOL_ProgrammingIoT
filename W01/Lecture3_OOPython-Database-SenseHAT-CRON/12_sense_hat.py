# Reading pressure with the Sense HAT

from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

pressure = sense.get_pressure()
print(pressure)

# temperature

sense.clear()

temp = sense.get_temperature()
print(temp)

# humidity

sense.clear()

humidity = sense.get_humidity()
print(humidity)