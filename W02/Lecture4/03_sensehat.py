from sense_hat import SenseHat

sense = SenseHat()
temp1 = sense.get_temperature_from_humidity()
print("Temperature: %s C" % temp1)

temp2 = sense.get_temperature_from_pressure()
print("Temperature: %s C" % temp2)

pressure = sense.get_pressure()
print("Pressure: %s Millibars" % pressure)

# Alternatives.
print(sense.pressure)

# IMU sensors.
orientation = sense.get_orientation_degrees()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

orientation = sense.get_orientation()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

# Alternatives.
print(sense.orientation)

north = sense.get_compass()
print("North: %s" % north)

# Alternatives.
print(sense.compass)

# Gyroscope.
gyro_only = sense.get_gyroscope()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))

# Alternatives.
print(sense.gyro)
print(sense.gyroscope)

# Accelerometer.
accel_only = sense.get_accelerometer()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only))

# Alternatives.
print(sense.accel)
print(sense.accelerometer)
