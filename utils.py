# face detection from webcam

import numpy as np
import cv2


# haar cascade classifier
haar = cv2.CascadeClassifier('./app/data/haarcascade_frontalface_default.xml')


def pipeline_model():
    def face_detect(img):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = haar.detectMultiScale(gray, 1.3, 5)

        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        return img


    # load the video
    cap = cv2.VideoCapture(0)

    # fps means frames per second and it is difficult to capture so many frames therefore we are using a while loop
    while True:
        ret, frame = cap.read()
        # ret will return true if the video can be read
        # frame is our single image
        

        frame = face_detect(frame)
        if ret:
            if cv2.waitKey(30):
                cv2.imwrite('./app/data/taken_img1.png', frame)
        else:
            break
        cv2.imshow('object_detect', frame)
        

        # we have suppose 24 fps then we have to run the loop for 40/30 ms
        if cv2.waitKey(30) == 27:
            # 27 is the number of escape key
            break
    cv2.destroyAllWindows()
    # releasing the captured image
    cap.release()
    return frame


