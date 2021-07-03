import numpy as np
import cv2

cap = cv2.VideoCapture(0)
back = cv2.imread('./image.jpg')

while cap.isOpened():
    #take each frame
    ret, frame = cap.read()

    if ret == True:
        #coverting rgb to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #cv2.imshow('hsv', hsv)

        #threshold value of hsv to get only red
        l_red =  np.array([0,100,100])
        u_red = np.array([10,255,255])

        mask = cv2.inRange(hsv, l_red, u_red)
        #cv2.imshow("mask", mask)

        part1 = cv2.bitwise_and(back, back, mask = mask)
        mask = cv2.bitwise_not(mask)
        part2 = cv2.bitwise_and(frame, frame, mask = mask)

        cv2.imshow("cloak", part1 + part2)
        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()