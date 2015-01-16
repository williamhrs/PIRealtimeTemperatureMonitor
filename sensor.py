import time
from urllib2 import Request, urlopen
import Adafruit_MCP9808.MCP9808 as MCP9808
sensor = MCP9808.MCP9808()

sensor.begin()

timestamp = lambda: int(round(time.time() * 1000))
temp = sensor.readTempC()
values = { 'data': { 'temp' : temp, 'timestamp' : timestamp() } }
# REST API uses an additional header - "Appbase-Secret"
headers = {
  'Content-Type': 'application/json',
  'Appbase-Secret': '9d7f14bc1ecabc8b47ed176e4e1772cd'
}
                              

# Send "PATCH" request to create or update a resource.
request = Request('https://api.appbase.io/tempmonitor/v2/pi/temperature', data=values, headers=headers)
request.get_method = lambda: 'PATCH'
urlopen(request).read()

#while True:
#    temp = sensor.readTempC()
#    print temp
#    time.sleep(5.0)
	