import cv2

# the convention of x and y axes in opencv:

"""
(0,0) -----------> X 
      |
      |
      |
      v
      Y
 """

# ******************** Converting the image to grayscale ********************

# in order to resize an image we need to know the current size of the image

# import an image
img = cv2.imread("Resources/snow_in_Bolivia.png")

# print the size of the image: (height, width, number of channels - BGR=3)
print(img.shape)

# arguments of the functions resize - 1) the image, 2) (height, width)
# imgResize = cv2.resize(img, ())

cv2.imshow("image", img)
cv2.waitKey(0)
