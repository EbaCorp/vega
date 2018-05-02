import time
from espeak import espeak
from espeak import core as espeak_core

# Calling shell commands
from subprocess import call

# Config 
speech_speed = 140 # words per minute

espeak.set_parameter(espeak.Parameter.Rate, speech_speed, False)

def synth(*args):
	done_synth=[False]
	def cb(event, pos, length):
		if event == espeak_core.event_MSG_TERMINATED:
			done_synth[0] = True
	espeak.set_SynthCallback(cb)
	r = espeak.synth(*args)
	call(["reset"]) # Clear Output
	print "Copyright by EBA GROUP (TM)",
	print "\r\n"
	while r and not done_synth[0]:
		time.sleep(0.05)
	return r

synth("To the Moon!")

