'''
installing external module 
"pyttsx" module for speech text to voice
    for male and female voice
'''

import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Function to set voice
def set_voice(voice_type="male"):
    if voice_type.lower() == "male":
        engine.setProperty('voice', voices[0].id)  # Male voice
    else:
        engine.setProperty('voice', voices[1].id)  # Female voice

# Set to Male voice and speak
set_voice("male")
engine.say("Hello Aashish, this is a male voice.")
engine.runAndWait()

# Set to Female voice and speak
set_voice("female")
engine.say("Hello Aashish, this is a female voice.")
engine.runAndWait()
