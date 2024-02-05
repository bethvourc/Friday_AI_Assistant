import os
import time  
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr

api_key = "PUT_IN_API_KEY"

# language AI will use
lang = "en"

openai.api_key = api_key

while True:
    def get_audio():
        r = sr.Recognizer() # using speach recognition
        with sr.Microphone(device_index=1) as source: # set up our Microphone
            audio = r.listen(source) # listens to the audio
            said = "" # to store the audio that comes in 

            # to make the computer listen for keyword to active (an example will be apples "hey siri")
            try:
                said = r.recognize_google(audio)
                print(said)

                if "Friday" in said:
                    completion = openai.ChatCompletion.create(model="gpt-4-turbo", messages=[{"role": "user", "content": said}])
                    text = completion.choices[0].messages.content
                    speech = gTTS(text=text, lang=lang, slow=False, tld="com.au") # tld is used to get the accent that the AI will use 
                    speech.save("welcome1.mp3")
                    playsound.playsound("welcome1.mp3")

            except Exception:
                print("Exceptions")

        return said
    
    get_audio()
