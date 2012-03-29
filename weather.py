#!/usr/bin/python
# -*- coding: utf-8 -*-

# weather.py
# By: Lorenzo Bivens at gmail dot com 
# License: Public Domain
#
# Gets the weather and returns a string
# Why? Because I want a cute weather indicator in my prompt
# To Do? A lot of stuff

import os
import sys
import pycurl
import StringIO
from xml.dom.minidom import parseString

# Look here if you need to configure something
ZIPCODE = "10601"
WURL = "http://www.google.com/ig/api?weather="
UNIT = 'C'

# General Initialization
wbuffer = StringIO.StringIO()

# Curl initialization
wcurl = pycurl.Curl()
wcurl.setopt(pycurl.URL, WURL+ZIPCODE)
wcurl.setopt(pycurl.WRITEFUNCTION, wbuffer.write)

# Information fetch & parse
wcurl.perform()
dom = parseString(wbuffer.getvalue())

# Weather dictionary
# note that since google has not documented their API 
# I could be missing some weather
wconditions = { 'Clear': "☉",
				'Chance of Rain': "☂",
				'Sunny': "?",
				'Mostly Sunny': "?",
				'Partly Cloudy': "☁?",
				'Mostly Cloudy': "☁☁",
				'Chance of Storm': "☁☂",
				'Showers': "☂",
				'Rain': "☔",
				'Chance of Snow': "☃",
				'Cloudy': "☁",
				'Mist': "#",
				'Storm': "☈",
				'Thunderstorm': "☈",
				'Chance of Storm': "☁?",
				'Sleet': "S",
				'Snow': "☃",
				'Icy': "I",
				'Dust': "D",
				'Fog': "#",
				'Smoke': "S",
				'Haze': "H",
				'Flurries': "*",
				'Overcast': "☁"}



# prepare output
wsymbol = wconditions.get(dom.getElementsByTagName('condition')[0].getAttribute('data'))

if UNIT == 'F':
	temp = dom.getElementsByTagName('temp_f')[0].getAttribute('data')
else:
	temp = dom.getElementsByTagName('temp_c')[0].getAttribute('data')
	
# and now the end
print '%s %d°%s' % (wsymbol, int(temp), UNIT)

wbuffer.close()









