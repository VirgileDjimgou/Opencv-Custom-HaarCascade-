import cv2
from datetime import datetime
  
class Webcam(object):
  
    WINDOW_NAME = "Playing Card Detection System"
  
    # constructor
    def __init__(self):
        self.webcam = cv2.VideoCapture(1)       
 
    # save image to disk
    def _save_image(self, path, image):
        filename = datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss%f') + '.jpg'
        cv2.imwrite(path + filename, image)
  
    # detect cards in webcam
    def detect_cards(self, cascade_path):
  
        # get image from webcam
        img = self.webcam.read()[1]
          
        # do card detection
        card_cascade = cv2.CascadeClassifier(cascade_path)
  
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        cards = card_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(200, 300))
  
        for (x,y,w,h) in cards:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
  
        # save image to disk
        self._save_image('WebCam/Detection/', img)
  
        # show image in window
        cv2.imshow(self.WINDOW_NAME, img)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
          
        # indicate whether cards detected
        if len(cards) > 0:
            return True
  
        return False
