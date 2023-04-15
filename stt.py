import speech_recognition as sr
import os
import openai
import sounddevice
from scipy.io.wavfile import write

def Recognition(nation):
    r = sr.Recognizer()
    harvard = sr.AudioFile('./test.wav')
    with harvard as source:
        audio = r.record(source)
        try:
            a = r.recognize_google(audio,language=nation)
            print(a)
            return a
        except Exception as e:
            print("Exception : "+str(e))
            return 0

def voice_recorder(seconds, file):
    print("Recording Started…")
    recording = sounddevice.rec((seconds * 44100), samplerate= 44100, channels=2)
    sounddevice.wait()
    write(file, 44100, recording)
    print("Recording Finished")

openai.api_key = ""
nation = 'ko-KR'

voice_recorder(10, "test.wav")
text = Recognition(nation)
response = openai.Completion.create(engine="text-davinci-002",
                                    prompt=text,
                                    max_tokens=150)
answer = response.choices[0].text.strip() # text 앞뒤 공백을 제거
print(f"답변 : {answer}")

os.remove('test.wav')







