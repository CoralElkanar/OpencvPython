import pathlib
import cv2

# another way to create a face detector:
# I imported 'pathlib' in order to find the xml file - for cases we do not have the file in our resources

# load the face cascade classifier
cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
face_classifier = cv2.CascadeClassifier(str(cascade_path))

# image data will be the camera data (0 is the default camera)
camera = cv2.VideoCapture(0)

# *************************************************************************

# # another way - using a video
# camera = cv2.VideoCapture("Resources/video")

# ************************************************************************************

while True:
    _, frame = camera.read()
    # '_' means - ignore the returned value from this loop

    # convert the frame to grayscale:
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces from the input video -
    # scaleFactor - scale the image by a factor of 1.1
    # minNeighbors - the higher this number, the more strict the criteria is going to be,
    # the  smaller the number, the more faces we'll find, but also we might find False objects.
    faces = face_classifier.detectMultiScale(frameGray, scaleFactor=1.1, minNeighbors=5,
                                             minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    # draw rectangles around detected faces:
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 0, 255), 2)

    # display the frame with face rectangles:
    cv2.imshow("Faces", frame)

    # exit the loop when 'q' is pressed:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video capture and close all openCV windows
camera.release()
cv2.destroyAllWindows()
