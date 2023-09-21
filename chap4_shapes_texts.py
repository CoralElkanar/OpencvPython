import cv2
import numpy as np

# create a matrix of zeros - zero means BLACK!
# 1) dimensions: (height, width) - 512x512 = grayscale image
# 2) num of channels:  3 channels - adding the color functionality
# 3) num of bits: uint8 - 8 bits - the values range from 0 to 255
img = np.zeros((512, 512, 3), np.uint8)

# check the dimensions of the image
print(img.shape)

cv2.imshow("Black Image", img)
cv2.waitKey(0)

# ************************* color the image *************************
# example:
# the colored part will be in the range we defined, and also, it's changing the img permanently
# img[200:300, 100:300] = 0, 0, 255  # BLUE=255, GREEN=0, RED=0

# [:] - means the whole image
img[:] = 255, 0, 0  # BLUE=255, GREEN=0, RED=0

cv2.imshow("Blue Image", img)
cv2.waitKey(0)

# ********************** add a line to the image **********************

# line function -
# 1) the image
# 2) starting point and ending point as (x,y)
# 3) the color of the line (B,G,R)
# 4) not essential - thickness
cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 3)

cv2.imshow("Image with green line", img)
cv2.waitKey(0)

# if we want to bring the line until the end of the image using the shape function -
# img.shape[height,width,num of channels]
# the end of the matrix -(x,y) = (width,height) = (img.shape[1],img.shape[0])

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.imshow("Image with diagonal green line", img)
cv2.waitKey(0)

cv2.destroyAllWindows()

# ******************* add a rectangle to the image *******************

# rectangle function -
# 1) the image
# 2) define the points
# 3) define the color (B,G,R)
# 4) thickness defined in numbers or, if we want it to be filled write 'cv2.FILLED'
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)

cv2.imshow("Image with a red rectangle", img)
cv2.waitKey(0)

# ******************** add a circle to the image ********************

# circle function -
# 1) the image
# 2) the center point of the circle
# 3) radius
# 4) color
# 5) thickness

cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)
cv2.imshow("Image with a light blue circle", img)
cv2.waitKey(0)

# ********************** add text to the image **********************

# putText function -
# 1) the image
# 2) the text
# 3) the origin point
# 4) define the font - write "cv2.FONT" and then choose from the options
# 5) font scale
# 6) color
# 7) thickness
cv2.putText(img, " OPENCV ", (300, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 150, 150), 3)

cv2.imshow("Image with text", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
