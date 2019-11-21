# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import serial
	

# Create your views here.
def Monitor(request):
	try:
		arduino=serial.Serial("/dev/ttyUSB0",timeout=5,baudrate=115200)
	except:
		print "hello"
	st=str(arduino.read(8566))
	return HttpResponse(st)
