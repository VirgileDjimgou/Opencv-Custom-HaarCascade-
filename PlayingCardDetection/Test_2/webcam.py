import cv2
from datetime import datetime
  
class Webcam(object):
  
    WINDOW_NAME = "Playing Card Detection System"
     
    # constructor
    def __init__(self):
        self.webcam = cv2.VideoCapture(0)       
 
    # save image to disk
    def _save_image(self, path, image):
        filename = datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss%f') + '.jpg'
        cv2.imwrite(path + filename, image)
 
    # rotate image
    def _rotate_image(self, roi_gray):
        (h, w) = roi_gray.shape[:2]
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, 180, 1.0)
        return cv2.warpAffine(roi_gray, M, (w, h))
 
    # detect cards in webcam
    def detect_cards(self, card_path, motif_path, motif_number):
        isDetected = False
         
        # get image from webcam
        img = self.webcam.read()[1]
          
        # do card detection
        card_cascade = cv2.CascadeClassifier(card_path)
        motif_cascade = cv2.CascadeClassifier(motif_path)
 
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        cards = card_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(200, 300))
 
        for (x,y,w,h) in cards:
            current_motif_number = 0
             
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
 
            roi_gray = gray[y:y+h, x:x+w]
            current_motif_number += len(motif_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=110))
                 
            roi_gray = self._rotate_image(roi_gray)
            current_motif_number += len(motif_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=110))
               
            print(current_motif_number)
            if current_motif_number == motif_number:
                isDetected = True
 
        # save image to disk
        self._save_image('WebCam/Detection/', img)
  
        # show image in window
        cv2.imshow(self.WINDOW_NAME, img)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
          
        # indicate whether cards detected
        return isDetected
