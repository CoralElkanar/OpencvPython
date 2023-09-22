import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

cv2.imshow("cards image", img)
cv2.waitKey(0)

# we want to crop the spade king card from the image as flat as we can.
# in order to do that we need to define the 4 points of the card.

# a card is usually 2.5 by 3.5, so we keep this ratio
width, height = 250, 350


# [top left][top right][bottom left][bottom right]
# by opening the image in 'paint' app we can find the coordinates in the bottom right corner of the app
# when hovering with the cursor over the relevant points.

pts1 = np.float32([[92, 191], [251, 160], [132, 422], [308, 383]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# warpPerspective - (source image, matrix, (width, height))
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Output image - spade king card - using warp perspective", imgOutput)
cv2.waitKey(0)

cv2.destroyAllWindows()
