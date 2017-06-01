#!/usr/bin/env python
import requests
import json
import sys
import getopt

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

if mode == 'power':
	ledMaxHD = {'blue': 23137, 'uv': 8577, 'cool_white': 32272, 'royal': 33350, 'deep_red': 6950, 'green': 8769, 'violet': 8654}
	ledMaxNo = {'blue': 19975, 'uv': 7270, 'cool_white': 23592, 'royal': 23888, 'deep_red': 3768, 'green': 4190, 'violet': 7317}
	
	ledNowReq = requests.get("http://" + host + "/api/colors")
	ledNowVal = json.loads(ledNowReq.text)

	watts = 0.0
	for key, value in ledMaxNo.iteritems():
		watts = watts + (value/100 * ledNowVal[key]/10)

	print(watts/1000)

else:
	print("Modes are: leds, power")
