import cv2
import numpy as np

# the purpose is to put all the images in one window

# issues with the numpy horizontal/vertical stack methods:
# 1) we cannot resize the images so in some cases the images might go out of the frame of our screen
# 2) if the images do not match in the number of channels (for example: they're not both RGB) it won't work.

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
                    img_array[x][y] = cv2.resize(img_array[x][y],
                                                 (img_array[0][0].shape[1], img_array[0][0].shape[0]),
                                                 None, scale, scale)
                if len(img_array[x][y].shape) == 2:
                    img_array[x][y] = cv2.cvtColor(img_array[x][y], cv2.COLOR_GRAY2BGR)

        image_blank = np.zeros((height, width, 3), np.uint8)
        hor = [image_blank] * rows
        hor_con = [image_blank] * rows
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


# we're going to stack the image with itself:
img = cv2.imread("Resources/Sky.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# the arguments we pass to the function are -
# 1) the scale (we can scale them all up or down)
# 2) define the matrices of the images:
# horizontal stack: the images in the first row [], vertical stack: the number of added rows
# we have to match the number of images in each added row

imgStack = stack_images(0.5, ([img, imgGray, img], [img, img, img]))

# numpy horizontal stack function, as parameters we enter the images we want to stack
imgHor = np.hstack((img, img))

# numpy vertical stack function
imgVer = np.vstack((img, img))

cv2.imshow("2 images stacked horizontally", imgHor)
cv2.imshow("2 images stacked vertically", imgVer)
cv2.imshow("3 images stacked - scaled down, using the stack_images function", imgStack)

cv2.waitKey(0)
cv2.destroyAllWindows()
