"""
In this script, I've created a basic computer vision application using the OpenCV library.
It enables video capture from the computer's camera or webcam and applies color filtering based on
the HSV (Hue, Saturation, Value) color space.
The unique feature is the interactive color filter adjustment using trackbars, which allows to detect objects in
real-time based the desired color range.
"""

import cv2
import numpy as np

# initialize the webcam
cap = cv2.VideoCapture(0)

# set the frame width and height for the video capture
frameWidth = 640
frameHeight = 480
cap.set(3, frameWidth)
cap.set(4, frameHeight)


# define an empty callback function to be used for trackbars
def empty(a):
    pass


# create an HSV (Hue, Saturation, Value) color space window and set its size:
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)

# create trackbars for adjusting the HSV range for color filtering
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)


# create a loop for video capturing and processing
while True:
    # read a frame from the webcam
    success, img = cap.read()

    # convert the captured frame from BGR to HSV
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # retrieve the current trackbar values - to be saved to use in the paint project
    h_min = cv2.getTrackbarPos("Hue Min", "HSV")
    h_max = cv2.getTrackbarPos("Hue Max", "HSV")
    s_min = cv2.getTrackbarPos("Sat Min", "HSV")
    s_max = cv2.getTrackbarPos("Sat Max", "HSV")
    v_min = cv2.getTrackbarPos("Value Min", "HSV")
    v_max = cv2.getTrackbarPos("Value Max", "HSV")

    # define lower and upper bounds for the HSV color range
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # create a mask to filters out colors outside the specified HSV range
    mask = cv2.inRange(imgHsv, lower, upper)

    # apply the mask to the original frame to highlight the selected color
    result = cv2.bitwise_and(img, img, mask=mask)

    # convert the masked image to grayscale
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    # Stack the images horizontally and display them, when the 'q' key is pressed - exit
    hStack = np.hstack([img, mask, result])
    cv2.imshow('Horizontal Stacking', hStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
