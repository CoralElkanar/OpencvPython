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

# ******************** Resizing the image ********************

# in order to resize an image we need to know the current size of the image

# import an image
img = cv2.imread("Resources/snow_in_Bolivia.png")

# print the size of the image: (height, width, number of channels - BGR=3)
print(img.shape)

# arguments of the functions resize - 1) the image, 2) (width, height)
# we can decrease the number of pixels
imgResizeS = cv2.resize(img, (500, 350))
print(imgResizeS.shape)

# we can also increase the number of pixels, but it will not increase the quality
imgResizeL = cv2.resize(img, (1500, 1100))
print(imgResizeL.shape)

cv2.imshow("image", img)
cv2.imshow("Resized image - decreased number of pixels", imgResizeS)
cv2.imshow("Resized image - increased number of pixels", imgResizeL)

cv2.waitKey(0)
cv2.destroyAllWindows()


# ******************** Cropping the image ********************

# in order to crop the image, we can use the matrix functionality, since the image is an array of pixels
# [height, width]
imgCropped = img[0:200, 300:500]

cv2.imshow("Cropped image", imgCropped)
cv2.waitKey(0)
