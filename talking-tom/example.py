import imp
from src import TalkingTom
import time

if __name__ == "__main__":
    talkingTom = TalkingTom()
    while True:
        talkingTom.listenAndRepeat()
        time.sleep(0.5)
