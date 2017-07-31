#!/usr/bin/env python

'''
Object detection using haar cascades custum code djimgou patrick virgile

'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2

# local modules
from video import create_capture
from common import clock, draw_str


def detect(img, cascade):
    
    #gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    #cards = card_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(200, 300))
    rects = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=4, minSize=(200, 300),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

if __name__ == '__main__':
    import sys, getopt
    print(__doc__)

    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    try:
        video_src = video_src[2]
    except:
        video_src = 0

    # define custum source video
    # debug camera when two camera
    # when 0 = native camera (camera one) or when 1 (camera two)
    video_src = 0 
    print(str(video_src))
    args = dict(args)
    cascade_fn = args.get('--cascade', "haarcascade_Qhearts.xml")
    nested_fn  = args.get('--cascade', "myhaar.xml")

    cascade = cv2.CascadeClassifier(cascade_fn)
    nested = cv2.CascadeClassifier(nested_fn)

    cam = create_capture(video_src, fallback='synth:bg=../data/lena.jpg:noise=0.05')

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        t = clock()
        rects = detect(gray, cascade)
        vis = img.copy()
        draw_rects(vis, rects, (0, 255, 0))
        if not nested.empty():
            for x1, y1, x2, y2 in rects:
                roi = gray[y1:y2, x1:x2]
                vis_roi = vis[y1:y2, x1:x2]
                subrects = detect(roi.copy(), nested)
                draw_rects(vis_roi, subrects, (255, 0, 0))
        dt = clock() - t

        draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))
        cv2.imshow('Detection', vis)

        if cv2.waitKey(5) == 27:
            break
    cv2.destroyAllWindows()
