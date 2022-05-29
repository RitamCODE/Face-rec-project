# registration for first time users

import numpy as np
import cv2

# haar cascade classifier
haar = cv2.CascadeClassifier('./app/data/haarcascade_frontalface_default.xml')


def pipeline_model3():
    def face_detect(img):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = haar.detectMultiScale(gray, 1.3, 5)

        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        return img

    v=0
    # load the video
    cap = cv2.VideoCapture(0)

    # fps means frames per second and it is difficult to capture so many frames therefore we are using a while loop
    while True:
        ret, frame = cap.read()
        # ret will return true if the video can be read
        # frame is our single imag

        frame = face_detect(frame)
        if ret:
            v=1
            if cv2.waitKey(60):
                cv2.imwrite('./app/data/taken_img.png', frame)
        else:
            break
        cv2.imshow('object_detect', frame)
        

        # we have suppose 24 fps then we have to run the loop for 40 ms
        if cv2.waitKey(40) == 27:
            # 27 is the number of escape key
            break
    cv2.destroyAllWindows()
    # releasing the captured image
    cap.release()
    return v


