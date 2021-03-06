#!/usr/bin/python
#coding: utf-8
##############################################################################
# File:     cam-test.py
# Author:   Kleber Lima da Silva
# Version:  V0.1.0
# Date:     30-May-2017
# Brief:    Script for testing the USB Webcam
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

import sys
import cv2  # apt-get install python-opencv
from pydrive.auth import GoogleAuth     # pip install PyDrive
from pydrive.drive import GoogleDrive

filename = sys.argv[1] + '.jpg'

# Create local webserver and auto handles authentication.
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

# Google Drive object
drive = GoogleDrive(gauth)

# Webcam - OpenCV
cam = cv2.VideoCapture(0)

# Take a photo
s, im = cam.read()
cv2.imwrite(filename, im)
cv2.VideoCapture(0).release()

# Send the photo to Google Drive
file1 = drive.CreateFile()
file1.SetContentFile(filename)
file1.Upload()
print('Created file %s with mimeType %s' % (file1['title'],
file1['mimeType']))
