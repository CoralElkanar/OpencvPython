import cv2
import numpy as np

# in this chapter we will learn how to detect shapes in an image


# ********************************* functions *********************************


def stack_images(scale, img_array):
    """
    this function helps deal with the issues occur when we try to stack images that do not match in size or in channels
    :param scale:
    :param img_array:
    :return: ndarray
    """
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


def get_contours(image):
    # findContours parameters:
    # 1) the image
    # 2) retrieval method - we chose to use cv2.RETR_EXTERNAL - this method retrieves the extreme outer contours
    # 3) approximation - request for all the information or for compressed values, for this example we're going to get
    # all the contours that we've found - CHAIN_APPROX_NONE

    contours, heirarcy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # create a copy of the original image, so we can draw the contours on it
    for cnt in contours:
        # for each contour we will find its area:
        area = cv2.contourArea(cnt)
        # next step is to draw the contour
        print(area)

        # the parameter for the drawContours function:
        # 1) the image we want to draw the contours on
        # 2) the contours to draw
        # 3) the index of the contour to draw: we inserted '-1' in order to draw all the contours
        # 4) color of the contour (B,G,R)
        # 5) thickness of the contour

        # define a threshold of the minimal area size (in pixels) - in order to ignore noises (500 chosen randomly)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)

            # calculate the curve length - that will help us approximate the corners of our shapes
            # the shapes are closed, so we will put 'True' as the second argument
            cnt_lng = cv2.arcLength(cnt, True)

            # approximate how many corner points we have for each contour:
            # the function return the values of the corner points for each contour
            # parameters: 1) contour, 2) resolution, 3) True - because the curve is closed
            approx = cv2.approxPolyDP(cnt, 0.02*cnt_lng, True)
            print(len(approx))

            object_corner = len(approx)

            # get the values of each of the shapes using the boundingRect function
            x, y, w, h = cv2.boundingRect(approx)

            # detect the object type by the number of corners
            if object_corner == 3:
                object_type = "Triangle"
            elif object_corner == 4:
                aspect_ratio = w/float(h)
                if 0.95 < aspect_ratio < 1.05:
                    object_type = "Square"
                else:
                    object_type = "Rectangle"
            elif object_corner > 4:
                object_type = "Circ"
            else:
                object_type = "None"

            # create a bounding boxes around each of the shapes that we detected
            # 1) the image we want to draw on, 2) two points for the rectangle, 3) color, 4) thickness
            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 1)

            cv2.putText(imgContour, object_type, (x+(w//2)-25, y+(h//2)),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)

# ************************************************************************************


path = 'Resources/shapes.png'

# first step - convert the image to greyscale
# second step - blur the gray scale image
# find the edges - use the canny edge detector

img = cv2.imread(path)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)

imgCanny = cv2.Canny(imgBlur, 200, 200)

imgContour = img.copy()

imgBlank = np.zeros_like(img)

get_contours(imgCanny)

imgStack = stack_images(0.6, ([img, imgGray, imgBlur], [imgCanny, imgContour, imgBlank]))
cv2.imshow('Original, Grayscale, Blur, Canny, Contours', imgStack)

cv2.waitKey(0)
