import cv2 
import os
import glob

for filename in glob.glob("dataset/*.jpg"):
        src = cv2.imread(filename)
        img = cv2.resize(src, (500,500))

        img = cv2.bilateralFilter(img,75,180,180)

        img = cv2.blur(img,(10,10))

        bb = 100
        ba = 255
        retval, dst = cv2.threshold(img,bb,ba, cv2.THRESH_BINARY_INV)

        imgAnd = cv2.bitwise_and(img, dst)

        cv2.imwrite(filename,imgAnd)

        cv2.waitKey()
        cv2.destroyAllWindows()    

