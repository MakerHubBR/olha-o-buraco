#!/usr/bin/python
#coding: utf-8
##############################################################################
# File:     gps-test.py
# Author:   Kleber Lima da Silva
# Version:  V0.1.0
# Date:     18-May-2017
# Brief:    Script for testing the onboard (DragonBoard 410c) GPS
################################################################################
# The MIT License (MIT)
#
# Copyright (c) 2017, Kleber Lima da Silva
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
################################################################################

import os
import serial   # pip install pyserial
import pynmea2  # pip install pynmea2 - https://github.com/Knio/pynmea2


def startGPS():
    os.system('sudo systemctl start qdsp-start.service')
    os.system('sudo systemctl start gnss-gpsd.service')
    os.system('sudo systemctl start qmi-gps-proxy.service')
    os.system('sudo systemctl restart gpsd')


def main():
    # Starts all services to enable GPS
    startGPS()

    # Open the GPS serial port
    gps = serial.Serial('/dev/ttyGPS0')

    while True:
        # Read and parse GPS data
        data = gps.readline()
        i = data.find('$GPGGA')
        if (i > 0):
            msg = pynmea2.parse(data[i:])
            print 'Latitude: ' + str(msg.latitude) + ' | Longitude: ' + str(msg.longitude)


if __name__ == '__main__':
    try:
        main()
    except FatalError as e:
        print '\nA fatal error occurred: %s' % e
        gps.close()
        sys.exit(2)
    except KeyboardInterrupt:
        print '\nExit'
        gps.close()
