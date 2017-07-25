from webcam import Webcam
 
webcam = Webcam()
  
# play a game of cards
while True:
  
    # attempt to detect the three of hearts
    if webcam.detect_cards('haarcascade_3hearts.xml') == True:
        print "I have the cotton picking three of hearts"
    else:
        print "I do not have the darn gun slinging three of hearts"
