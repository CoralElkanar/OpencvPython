import cv2
from hire_me import FaceImg

# in this chapter I'm going to use a method proposed by Viola 7 Jones

# This exercise requires a substantial dataset of images:
# Positives - Faces
# Negatives - Non Faces

# In theory, with these files we can train, and create a cascade file (XML File) that will assist in facial detection.

# However, in this tutorial, I will not be building the cascade from scratch.
# Instead, I will utilize a xml file for face detection provided by opencv.

# side note:
# opencv is providing some default cascades that can help detect different things such as number plates, eyes, etc.
# we have xml files provided by opencv for that purpose, they specify certain features, and certain filters for
# specific objects.

# add our faceCascede
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

img = cv2.imread('Resources/Engineer.png')
eng = FaceImg()
eng.put_text(img)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img2 = cv2.imread('Resources/BigBangTheory.PNG')
img2Gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

for image in [img, img2]:
    # find the faces in the image using the face cascade:
    # 1) the grayscale image, 2) the scale factor, 3) minimum neighbors
    faces = faceCascade.detectMultiScale(image, 1.3, 6)

    # create a bounding box around the faces we detected (and put rectangles around them):
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)


cv2.imshow('cookies', img)
cv2.waitKey(-1)

cv2.imshow('Face detection', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
