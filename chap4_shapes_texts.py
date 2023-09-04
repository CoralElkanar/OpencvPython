import cv2
import numpy as np

# create a matrix of zeros - zero means BLACK!
# (height, width)
# 512x512 = grayscale image
# 3 channels - adding the color functionality
# uint8 - 8 bits - the values range from 0 to 255
img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

cv2.imshow("Black Image", img)
cv2.waitKey(0)

# color the image
# [:] - means the whole image
img[:] = 255, 0, 0  # BLUE=255, GREEN=0, RED=0

cv2.imshow("Blue Image", img)
cv2.waitKey(0)



