import time
import urllib2 
import json
#import Adafruit_MCP9808.MCP9808 as MCP9808
#sensor = MCP9808.MCP9808()



#httplib.HTTPSConnection.debuglevel = 1

sensor.begin()

timestamp = lambda: int(round(time.time() * 1000))

while True:
	temp = sensor.readTempC()

	values = { 'data': { timestamp() : {"path":"temperature/"+timestamp() } } }
	# REST API uses an additional header - "Appbase-Secret"
	headers = {
	  'Content-Type': 'application/json',
	  'Appbase-Secret': '9d7f14bc1ecabc8b47ed176e4e1772cd'
	}
	                              
	# Send "PATCH" request to create or update a resource.
	request = urllib2.Request('https://api.appbase.io/tempmonitor/v2/pi/temperature/~edges', data=json.dumps(values), headers=headers)
	request.get_method = lambda: 'PATCH'
	try:
		x = urllib2.urlopen(request)
		print x.read()
	except urllib2.HTTPError, e:
		print e.hdrs
	time.sleep(5.0)
