#!/usr/bin/python
"""
author: matt venn, based on Adafruit's example
"""

from Adafruit_BMP085 import BMP085

#initialise the sensor
bmp = BMP085(0x77)

temp = bmp.readTemperature()
pressure = bmp.readPressure()
altitude = bmp.readAltitude()

print "Temperature: %.2f C" % temp
print "Pressure:    %.2f hPa" % (pressure / 100.0)
print "Altitude:    %.2f" % altitude
