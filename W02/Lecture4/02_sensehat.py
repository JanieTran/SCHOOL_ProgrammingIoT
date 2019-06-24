from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear(255, 127, 0)

print(sense.gamma)
time.sleep(2)

sense.gamma = sense.gamma[::-1]
print(sense.gamma)
time.sleep(2)

sense.gamma_reset()
sense.clear()
