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
	request = requests.get("http://" + host + "/api/colors")
	data = json.loads(request.text)
	print(data['violet'])

else:
	print("Modes are: leds, power")
