#!/usr/bin/env python
import requests
import json
import sys
import getopt

# constants
ledMaxHD = {'blue': 23137, 'uv': 8577, 'cool_white': 32272, 'royal': 33350, 'deep_red': 6950, 'green': 8769, 'violet': 8654}
ledMaxNo = {'blue': 19975, 'uv': 7270, 'cool_white': 23592, 'royal': 23888, 'deep_red': 3768, 'green': 4190, 'violet': 7317}

# variables
host = ''
mode = ''

myopts, args = getopt.getopt(sys.argv[1:], "h:m:")

for option, argument in myopts:
	if option == '-h':
		host = argument
	elif option == '-m':
		mode = argument
	else:
		print("Usage: %s -h host -m mode" % sys.argv[0])

if mode == 'leds':
        ledNowReq = requests.get("http://" + host + "/api/colors")
        ledNowVal = json.loads(ledNowReq.text)

	leds = " ".join(["=".join([key, str(val*1.0/10)]) for key, val in ledNowVal.items()])

	print("OK - LED's: " + leds + " | " + leds)
	sys.exit(0)

elif mode == 'power':
	ledNowReq = requests.get("http://" + host + "/api/colors")
	ledNowVal = json.loads(ledNowReq.text)

	wattsByLed = {}
	watts = 0.0
	for key, value in ledMaxNo.iteritems():
		wattsByLed[key] = (value/100 * ledNowVal[key]/10)
		watts = watts + wattsByLed[key]

	perfWattsByLed = " ".join(["=".join([key, str(val*1.0/1000)]) for key, val in wattsByLed.items()])

	print("OK - " + str(watts/1000) + " Watt's are in use. | watt=" + str(watts/1000) + " " + perfWattsByLed)
        sys.exit(0)
else:
	print("UNKNOWN - Mode's are: leds, power")
	sys.exit(3)
