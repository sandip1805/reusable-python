import speech_recognition as sr
from playsound import playsound
import shutil
import os

class TalkingTom:

    def listenAndRepeat(self):
        with self.microPhone as source:
            print("Say something!")
            audio = self.recognizer.listen(source, phrase_time_limit=5)
            with open("recorded.wav", "wb") as file:
                file.write(audio.get_wav_data())            
            playsound("recorded.wav")

    def __init__(self) -> None:        
        self.recognizer = sr.Recognizer()
        self.microPhone = sr.Microphone()        