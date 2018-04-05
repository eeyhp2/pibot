from picamera import PiCamera
from picamera.array import PiRGBArray
import numpy as np
import cv2
import time

def capture():
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.vflip = True
    time.sleep(2)
    camera.capture('Image.png')
    camera.close()
    I = cv2.imread('Image.png', 0)
    I = cv2.resize(I, (0, 0), fx=0.4, fy=0.4)
    return I

def cannydetection(img):
	threshold = 100
    BW2 = cv2.Canny(img, threshold, threshold*0.4)
    cv2.imwrite('edge.jpg', BW2)
	return None
	
def houghdetection(img):
	BW3 = cv2.resize(cv2.imread('edge.jpg', BW2), (0, 0), fx=1/0.4, fy=1/0.4)
    #lines = cv2.HoughLinesP(BW3, 5, np.pi/180, 500, 100, 800, 200)
    lines = cv2.HoughLinesP(BW3, 1, np.pi/180, 200)
    I = cv2.imread('Image.png')
	for i in range(len(lines)):
        for x1, y1, x2, y2 in lines[i]:
            cv2.line(I, (x1, y1), (x2, y2), (0, 255, 0), 4)
        cv2.imwrite('houghlines.jpg', I)
	lines = lines.squeeze()
    size = BW3.shape
	return lines, size

def detectedges():
	#Capture image
	img = capture()
	
    #Canny edge detection
    cannydetection(img)
	
    #Hough Transform
    lines, size = houghdetection(img)

    return None

if __name__ == '__main__':
    detectedges()
    