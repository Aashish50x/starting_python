'''
installing external module 
"pyttsx" module for speech text to voice
    for female voice
'''

import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)
engine.setProperty('voice', voices[1].id)  # Female voice

# Text to be spoken
text = "Hello, Aashish! Welcome to Python text-to-speech."

# Speak the text
engine.say(text)

# Wait until the speaking is finished
engine.runAndWait()
