import cv2
import numpy as np

# we need to define some color values and ranges:  the hue, saturation and value ranges.
# if the image region falls within that color range, we will 'grab' that.

# we do not actually know what are the minimum and maximum values for a particular color we want to find.
# track bar - we will use them to 'play' around with the values in real time so that we can find the
# optimum minimum and maximum values.


def empty(a):
    pass

# ************************ function that deals with the issues ************************


def stack_images(scale, img_array):
    rows = len(img_array)
    cols = len(img_array[0])
    rows_available = isinstance(img_array[0], list)
    width = img_array[0][0].shape[1]
    height = img_array[0][0].shape[0]
    if rows_available:
        for x in range(0, rows):
            for y in range(0, cols):
                if img_array[x][y].shape[:2] == img_array[0][0].shape[:2]:
                    img_array[x][y] = cv2.resize(img_array[x][y], (0, 0), None, scale, scale)
                else:
                    img_array[x][y] = cv2.resize(img_array[x][y], (img_array[0][0].shape[1],
                                                                   img_array[0][0].shape[0]), None, scale, scale)
                if len(img_array[x][y].shape) == 2:
                    img_array[x][y] = cv2.cvtColor(img_array[x][y], cv2.COLOR_GRAY2BGR)
        image_blank = np.zeros((height, width, 3), np.uint8)
        hor = [image_blank]*rows
        hor_con = [image_blank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(img_array[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if img_array[x].shape[:2] == img_array[0].shape[:2]:
                img_array[x] = cv2.resize(img_array[x], (0, 0), None, scale, scale)
            else:
                img_array[x] = cv2.resize(img_array[x], (img_array[0].shape[1], img_array[0].shape[0]),
                                          None, scale, scale)
            if len(img_array[x].shape) == 2:
                img_array[x] = cv2.cvtColor(img_array[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(img_array)
        ver = hor
    return ver

# ***********************************************


path = 'Resources/Peru_lake.png'

cv2.namedWindow("TrackBars")

# resizing the size of the trackbars
cv2.resizeWindow("TrackBars", 640, 240)

# createTrackbar function -
# 1) define the name of the trackbar (what values we're going to change using this trackbar)
# 2) define which window we're going to put this trackbar on
# 3) the current value, what will be the initial value when the script runs
# 4) what will be the maximum value of the hue.
# hue values are from 0 to 360 , but in opencv - 0:179
# 5) we have to call this function every time something changes in these trackbars

cv2.createTrackbar("Hue Min", "TrackBars", 144, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 175, 179, empty)

# saturation trackbar
cv2.createTrackbar("Sat Min", "TrackBars", 125, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)

# value trackbar
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

# we're going to read these trackbars, so we could apply to our image
# getTrackbar position function - gets the values

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    # now that we have the ranges of min:max of the hue, saturation and values,
    # we'll use them to filter out our image to get the particular color in that range

    # create a mask in the ranges we found: (this mask will give us the filtered out image of that color)
    # 1) the image, 2) the minimum value, 3) the maximum value

    # create a numpy array for the minimum values and the max values of h,s,v
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(imgHSV, lower, upper)

    # when playing with the trackbars to find the color we are interested in,
    # we need to change them so the color will be presented in the masked image as white,
    # and all other colors will be black.

    # we now can present the original image combined with the mask that we created to show only the parts with the
    # chosen color
    # we'll use bitwise operation AND on the original image and the masked image,
    # where the pixels appear in white = True, and the pixels in black = False

    imgResult = cv2.bitwise_and(img, img, mask=mask)

    # cv2.imshow("original image", img)
    # cv2.imshow("HSV image", imgHSV)
    # cv2.imshow("Masked HSV image", mask)
    # cv2.imshow("Result image", imgResult)

    final = stack_images(0.6, ([img, imgHSV], [mask, imgResult]))

    cv2.imshow("Original, HSV, Masked, Result", final)

    cv2.waitKey(1)
