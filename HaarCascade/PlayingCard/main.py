from webcam import Webcam
 
webcam = Webcam()


#webcam.detect_cards_local()
  
# play a game of cards
while True:
  
    # attempt to detect the three of hearts
    if webcam.detect_cards('cascade.xml') == True:
        print("I have the cotton picking three of hearts")
    else:
        print("I do not have the darn gun slinging three of hearts")
