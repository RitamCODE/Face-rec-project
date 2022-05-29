# image comparison code starts here
import cv2
import numpy as np


def pipeline_model2():
    original = cv2.imread("./app/data/taken_img.png")
    duplicate = cv2.imread("./app/data/taken_img1.png")
    # 1) Check if 2 images are equals
    if original.shape == duplicate.shape:
        cv2.imshow("Original", original)
        cv2.imshow("Duplicate", duplicate)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return 1
    else:
        return 2
    #difference = cv2.subtract(original, duplicate)
    #b, g, r = cv2.split(difference)
    #if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
     #   print("The images are completely Equal")


