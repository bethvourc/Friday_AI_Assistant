import os
import time
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr

api_key = "PUT_IN_API_KEY"
lang = "en"

openai.api_key = api_key

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print("You said:", said)

            if "Friday" in said:
                completion = openai.Completion.create(engine="text-davinci-003", prompt=said, max_tokens=50)
                text = completion.choices[0].text.strip()
                speech = gTTS(text=text, lang=lang, slow=False, tld="com.au")
                speech.save("response.mp3")
                playsound.playsound("response.mp3")

        except Exception as e:
            print("Exception:", str(e))

    return said

def main():
    while True:
        get_audio()
        time.sleep(1)  # Prevents constant activation, adjust as necessary

if __name__ == "__main__":
    main()
