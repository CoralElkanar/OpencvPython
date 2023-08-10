# importing the computer vision package
import cv2

# if we succeeded to import the package, it will be printed -
print("Package Imported")


# ****************************** Reading an image and displaying it ******************************

# declaring the variable in which we will store the image
# 'imread' - function for reading the images
# the argument we supply to this function is the path to the image
img1 = cv2.imread("Resources/sky.png")

# 'imshow' - function for displaying the images
# two arguments - first one is the name of the window, second is the image we want to display
cv2.imshow("Output", img1)

# we need to add a delay so that the image would not close immediately.
# if we insert '0' as an argument, the delay will be infinite,
# if we insert a value it indicates the delay in milliseconds (1000 = 1 second)
cv2.waitKey(0)
