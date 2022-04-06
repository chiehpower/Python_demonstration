import cv2 

im = cv2.imread('qrcode.png')
det = cv2.QRCodeDetector()
retval, points, straight_qrcode = det.detectAndDecode(im)

print(retval, points, straight_qrcode)