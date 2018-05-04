#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Speech Utilities.

This module is responsible for any speech-to-text or text-to-speech
interactions with outer APIs/services.
"""


from subprocess import call
import time

from espeak import espeak
from espeak import core as espeak_core


SPEECH_SPEED = 30 # words per minute

espeak.set_parameter(espeak.Parameter.Rate, SPEECH_SPEED, False)
espeak.set_voice("ru") # Russian language interface

class Speech():
    """Method for audio output.
    
    We are passing data to outer RESTful API, then getting back response.
    Response is being synthesized. User hears output as an audio.
    """
    @staticmethod
    def say(*args):
        done_synth=[False]
        def cb(event, pos, length):
            if event == espeak_core.event_MSG_TERMINATED:
                done_synth[0] = True
        espeak.set_SynthCallback(cb)
        r = espeak.synth(*args)

        while r and not done_synth[0]:
            time.sleep(0.05)
        return r
