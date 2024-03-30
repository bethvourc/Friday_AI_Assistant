# print(sr.Microphone.list_microphone_names())

import os
import time
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr

api_key = "api-key"
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
                # Assuming `client` is correctly instantiated as shown in the documentation snippets
                client = openai.OpenAI(api_key=api_key)
                response = client.completions.create(
                    model="gpt-3.5-turbo",  # Adjust the model as necessary
                    prompt=said,
                    max_tokens=50
                )
                text = response['choices'][0]['text'].strip()
                speech = gTTS(text=text, lang=lang, slow=False, tld="com.au")
                speech.save("response.mp3")
                # Play the saved audio file
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
