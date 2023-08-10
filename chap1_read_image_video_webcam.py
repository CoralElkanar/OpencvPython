# importing the computer vision package
import cv2

# if we succeeded to import the package, it will be printed -
print("Package Imported")


# ****************************** Reading an image and displaying it ******************************

# declaring the variable in which we will store the image
# 'imread' - function for reading the images
# the argument we supply to this function is the path to the image
img1 = cv2.imread("Resources/Sky.png")

# 'imshow' - function for displaying the images
# two arguments - first one is the name of the window, second is the image we want to display
cv2.imshow("Output", img1)

# we need to add a delay so that the image would not close immediately.
# if we insert '0' as an argument, the delay will be infinite,
# if we insert a value it indicates the delay in milliseconds (1000 = 1 second)
cv2.waitKey(0)


# ****************************** Reading a video and displaying it ******************************

# creating a VideoCapture object (importing the video to an object)
# the argument we put is the path of the video
cap = cv2.VideoCapture("Resources/sky_video.mp4")

# a video is a sequence of images, so we need a while loop that will go over each frame one by one and display it.
while True:
    # save the current image in the img variable and inform if it was done successfully
    # success is a boolean variable - True/False
    success, img = cap.read()

    # resizing the images in the video to make it smaller
    # arguments: 1. the input image we want to resize.
    # 2. specifies the dimensions of the output image,
    # 'None' means that the function calculates the output dimensions based on fx, fy
    # 3. fx - the scaling factor for the width, fy - the scaling factor for height
    frame = cv2.resize(img, None, fx=0.5, fy=0.5)

    # show the result
    cv2.imshow("Video", frame)

    # adding a delay that waits for the keyboard press 'q' if we want to break out of the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
