import cv2
import numpy as np

# import an image
img = cv2.imread("Resources/sky.png")


# ******************** Converting the image to grayscale ********************

# define grayscale image, we use a function from cv2 -
# cvtColor - this function converts the image into different color spaces
# the arguments - 1. the image we want to convert, 2. define which color space we want it to be converted to
# RGB = BGR here, in the following - BGR to gray
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# display the grayscale image we created and add the delay, so it will not disappear form the screen
cv2.imshow("Gray Image", imgGray)
cv2.waitKey(0)


# ******************** blur function ********************

# declaring our blur image
# 1. first argument is the image we want to blur
# 2. ksize is the kernel size we define to the image - it has to be odd numbers!
# 3. sigma X
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

# display the grayscale blurred image we created and add the delay, so it will not disappear form the screen
cv2.imshow("Grayscale Blurred Image", imgBlur)
cv2.waitKey(0)


# ******************** edge detector function ********************

# this function finds the edges of our image
# the arguments for this function - 1. the image, 2 and 3. two thresholds
imgCanny = cv2.Canny(img, 100, 100)

# display the Canny image we created and add the delay, so it will not disappear form the screen
cv2.imshow("Canny Image", imgCanny)
cv2.waitKey(0)

# sometimes if we get a lot of edges we can reduce that
# to get less edges of the image = show fewer details =
# (looks like coloring pages for kids that present the characters as lines) we can change the value of the thresholds -
# increase the threshold

imgCanny2 = cv2.Canny(img, 150, 200)

# display the second Canny image we created and add the delay
cv2.imshow("Canny Image with less edges", imgCanny2)
cv2.waitKey(0)

# ******************** dilation function ********************

# sometimes we're detecting an edge but because there's a gap, or because it's not joined properly,
# it does not detect it as a proper line, so we can solve that by increasing the thickness of the edge.
# the arguments for this function are: 1. the Canny image
# 2. the kernel - it's a matrix we have to define the size of and the value of
# 3. how many iterations we want the kernel to move around - meaning, how thick we want the lines to be

# define the kernel as a matrix of ones: the arguments -
# 1) the size of the matrix
# 2) the type of the object - unsigned, the values can rate from 0 to 255 (8 bits)
kernel = np.ones((5, 5), np.uint8)

imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)

cv2.imshow("Dilation Image - thicker edges", imgDilation)
cv2.waitKey(0)


# ******************** erode function ********************

# this function makes the edges thinner, the arguments -
# 1) the image
# 2) the kernel
# 3) the number of iterations

imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow("Eroded Image - thinner edges", imgEroded)
cv2.waitKey(0)
