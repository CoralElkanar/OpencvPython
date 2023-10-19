"""in the following project I will create a virtual painter, using detection of the object shown on the webcam
and 'drawing' virtually with it. """

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# setting parameters to the captured object
frame_width = 640
cap.set(3, frame_width)
frame_height = 480
cap.set(4, frame_height)
brightness_level = 150
cap.set(10, brightness_level)

# for detecting the colors:
colors_list_detect = [['blue', 94, 253, 60, 120, 255, 255],
                      ['pink', 54, 99, 182, 173, 251, 255],
                      ['green', 59, 94, 107, 101, 251, 255]]

# for drawing the colors: (in BGR!)
colors_list_paint = [[196, 77, 77],    # blue
                     [178, 102, 255],  # pink
                     [76, 153, 0]]     # green


points_to_draw = []  # [x, y, color_index]


def color_detect(image, list_of_colors, colors_values_paint):
    # convert the image to HSV
    img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    new_points = []

    for i, color in enumerate(list_of_colors):
        # create a numpy array for the minimum values and the max values of h,s,v
        lower = np.array(color[1:4])  # [hue_min, sat_min, val_min]
        upper = np.array(color[4:7])  # [hue_max, sat_max, val_max]
        mask = cv2.inRange(img_hsv, lower, upper)
        x, y = get_contours(mask)

        # draw a circle at the top of the contour that we detected
        cv2.circle(img=img_result, center=(x, y), radius=7, color=colors_values_paint[i], thickness=cv2.FILLED)
        cv2.imshow(str(color[0]), mask)

        if x != 0 and y != 0:
            new_points.append([x, y, i])

    return new_points


def get_contours(image):
    # findContours parameters:
    # 1) the image
    # 2) retrieval method - we chose to use cv2.RETR_EXTERNAL - this method retrieves the extreme outer contours
    # 3) approximation - request for all the information or for compressed values, for this example we're going to get
    # all the contours that we've found - CHAIN_APPROX_NONE

    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    x, y, w, h = 0, 0, 0, 0

    # create a copy of the original image, so we can draw the contours on it
    for cnt in contours:
        # find the area of the contour:
        area = cv2.contourArea(contour=cnt)

        # the parameter for the drawContours function:
        # 1) the image we want to draw the contours on
        # 2) the contours to draw
        # 3) the index of the contour to draw: we inserted '-1' in order to draw all the contours
        # 4) color of the contour (B,G,R)
        # 5) thickness of the contour

        # define a threshold of the minimal area size (in pixels) - in order to ignore noises (500 chosen randomly)
        if area > 500:
            # check if the color pen is detected correctly - draw a contour around it
            # cv2.drawContours(image=img_result, contours=cnt, contourIdx=-1, color=(255, 0, 0), thickness=3)

            # calculate the curve length - that will help us approximate the corners of our shapes
            # the shapes are closed, so we will put 'True' as the second argument
            cnt_lng = cv2.arcLength(curve=cnt, closed=True)

            # approximate how many corner points we have for each contour:
            # the function return the values of the corner points for each contour
            # parameters: 1) contour, 2) resolution, 3) True - because the curve is closed
            approx = cv2.approxPolyDP(curve=cnt, epsilon=0.02*cnt_lng, closed=True)

            # get the values of each of the shapes using the boundingRect function
            x, y, w, h = cv2.boundingRect(array=approx)
    return x+w//2, y


def draw_on_screen(points_list, colors):
    for pnt in points_list:
        cv2.circle(img=img_result, center=(pnt[0], pnt[1]), radius=7, color=colors[pnt[2]], thickness=cv2.FILLED)


while True:
    # save the current image in the img variable and inform if it was done successfully
    # (success is a boolean variable - True/False
    success, img = cap.read()
    img_result = img.copy()

    points = color_detect(image=img, list_of_colors=colors_list_detect, colors_values_paint=colors_list_paint)
    if points:
        for point in points:
            points_to_draw.append(point)

    if points_to_draw:
        draw_on_screen(points_list=points_to_draw, colors=colors_list_paint)

    # display the result
    cv2.imshow("Video", img_result)

    # add a delay that waits for the keyboard press 'q' to break out of the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
