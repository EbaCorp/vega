# /usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple implementation for outer neural network's usage.

Sends request with desired text to host with neural network (in my case it was:
http://eba.cloud:8080/talk endpoint).

Retrieves data and then synthesizing it using my wrapper.

"""
import requests
import json

from . import Speech # Our wrapper

"""TODO: Wrap it up inside of a RESTful API
so we can access synthesizer from outside of 
our app (e.g. from mobile client).
"""
# Get input from user
INPUT_DATA = raw_input("Type text to-be-processed by neural network: ")

# Send POST request
r = requests.post('http://eba.cloud:8080/talk', json = {'text':INPUT_DATA} )
jr = json.loads(r.text)['answer'].encode('utf-8').strip()

Speech.say(jr)

print jr
