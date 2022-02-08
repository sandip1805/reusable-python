import speech_recognition as sr
from pydub import AudioSegment
from playsound import playsound



class TalkingTom:
    def listenAndRepeat(self):
        with self.microPhone as source:
            print("Say something!")
            audio = self.recognizer.listen(source, phrase_time_limit=5)
            with open("recorded.wav", "wb") as file:                                
                file.write(audio.get_wav_data())  
            self.updateSamplingRate()          
            playsound("recorded.wav")

    def updateSamplingRate(self) :
        sound = AudioSegment.from_file('recorded.wav', format="wav")
        # shift the pitch up by half an octave (speed will increase proportionally)
        octaves = 0.3
        new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))

        # keep the same samples but tell the computer they ought to be played at the 
        # new, higher sample rate. This file sounds like a chipmunk but has a weird sample rate.
        hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

        # now we just convert it to a common sample rate (44.1k - standard audio CD) to 
        # make sure it works in regular audio players. Other than potentially losing audio quality (if
        # you set it too low - 44.1k is plenty) this should now noticeable change how the audio sounds.
        hipitch_sound = hipitch_sound.set_frame_rate(44100)

        #export / save pitch changed sound
        hipitch_sound.export("recorded.wav", format="wav")

    def __init__(self) -> None:        
        self.recognizer = sr.Recognizer()
        self.microPhone = sr.Microphone()        