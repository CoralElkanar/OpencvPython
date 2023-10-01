"""

Hi, to anyone who has come across this project,

my name is Coral, I'm an electrical and electronics engineer, Tel-Aviv University graduate.

I have previously worked as a System Validation Engineer at Marvell Technology.

Currently, I am actively seeking my next exciting adventure.

"""

import cv2


class FaceImg(object):
    def put_text(self, image):
        cv2.putText(image, " Hire me :) ", (300, 170), cv2.FONT_HERSHEY_SIMPLEX, 1, (120, 0, 120), 3)

