"""
Author: Chieh

Source from: https://shengyu7697.github.io/python-opencv-puttext/

When we do the object detection, normally we will draw the class name for each bbox. 
In this code, we will introduce how to add the behind the words by cv2.
"""

import cv2 

if __name__=='__main__':

    img = cv2.imread('example.jpg')
    label = 'Object' 
    x1 = 330 
    y1 = 110
    x2 = 500
    y2 = 300
    cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 6)
    fontFace = cv2.FONT_HERSHEY_COMPLEX
    fontScale = 0.9
    thickness = 1
    labelSize = cv2.getTextSize(label, fontFace, fontScale, thickness)
    _x1 = x1 # bottomleft x of text
    _y1 = y1 # bottomleft y of text
    _x2 = x1+labelSize[0][0] # topright x of text
    _y2 = y1-labelSize[0][1] # topright y of text
    cv2.rectangle(img, (_x1,_y1), (_x2,_y2), (0,255,0), cv2.FILLED) # text background
    cv2.putText(img, label, (x1,y1), fontFace, fontScale, (0,0,0), thickness)

    cv2.imwrite("result.jpg", img)