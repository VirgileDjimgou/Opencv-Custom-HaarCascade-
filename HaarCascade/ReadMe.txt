
This repository contains haar cascade classifier files, related to the blog https://rdmilligan.wordpress.com

It also contains images on which to test out said xml classifiers

Please note that these classifiers are lightweight, created using a limited number of positive images. They have been created for "fun" so don't expect to build an industry-standard mission-critical system with them, as it might blow up. That said, if you can lay your hands on a large number of positive cropped images and want me to create a classifier for you, let me know. It can be loaded into this repository for others to have "fun" with

Subdirectory: Roundabout
Related post: https://rdmilligan.wordpress.com/2014/06/22/road-sign-detection-on-google-street-view/

Subdirectory: Commando
Related post: https://rdmilligan.wordpress.com/2014/09/04/detecting-objects-in-computer-games/

Subdirectory: PlayingCard
Related post: https://rdmilligan.wordpress.com/2014/08/30/playing-card-detection-using-opencv-mark-v/

Subdirectory: HandGesture
Related post: https://rdmilligan.wordpress.com/2015/03/29/voice-and-hand-gesture-recognition/

Subdirectory: Lego
Related post: https://rdmilligan.wordpress.com/2015/07/02/augmented-reality-using-opencv-and-python/

Subdirectory: Guitar
Related post: https://rdmilligan.wordpress.com/2014/05/29/guitar-detection-using-opencv-mark-iii/

Note: adjusting the parameters for the .detectMultiScale function can help with detection of objects. For example, lowering the value of the minNeighbors parameter will increase the likelihood of object detection (but will also increase the likelihood of false-positives)