#!/usr/bin/env python3
# -*- coding: utf-8 -*-z

import time
import urllib.request
import json
import Adafruit_MCP9808.MCP9808 as MCP9808
sensor = MCP9808.MCP9808()

sensor.begin()

timestamp = lambda: int(round(time.time() * 1000))

while True:
	temp = sensor.readTempC()
	curTimeStamp = str(timestamp())

	# REST API uses an additional header - "Appbase-Secret"
	headers = {
	  'Content-Type': 'application/json',
	  'Appbase-Secret': '9d7f14bc1ecabc8b47ed176e4e1772cd'
	}

	values = { 'data': { 'temperature' : temp, 'nowtimestamp':curTimeStamp } }
	# Send "PATCH" request to update properties
	request = urllib.request.Request('https://api.appbase.io/tempmonitor/v2/pi/temperature/'+curTimeStamp+'/~properties', data=json.dumps(values), headers=headers)
	request.get_method = lambda: 'PATCH'
	try:
		x = urllib2.urlopen(request)
		print(x.read())
		print("leitura1")
	except e:
		print(e)
	
	
	values = { 'data': { curTimeStamp : {"path":"pi/temperature/"+curTimeStamp } } }	                              
	# Send "PATCH" request to create an edge.
	request = urllib.request.Request('https://api.appbase.io/tempmonitor/v2/pi/temperature/~edges', data=json.dumps(values), headers=headers)
	request.get_method = lambda: 'PATCH'
	try:
		x = urllib2.urlopen(request)
		print(x.read())
		print("leitura2")
	except e:
		print(e)

	time.sleep(5.0)