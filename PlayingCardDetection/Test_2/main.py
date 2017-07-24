from webcam import Webcam
from speech import Speech
 
webcam = Webcam()
speech = Speech()
 
# play a game of cards
while True:
  
    # attempt to detect the three of hearts
    if webcam.detect_cards('haarcascade_3hearts.xml', 'haarcascade_heartmotif.xml', 3) == True:
        speech.text_to_speech("I have the cotton picking three of hearts")
    else:
        speech.text_to_speech("I do not have the darn gun slinging three of hearts")
