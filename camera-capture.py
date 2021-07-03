import cv2
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read() #reading from camera
    if ret == True:
        cv2.imshow("image", back)
        if cv2.waitKey(5) == ord('q'):
            cv2.imwrite('image.jpg', back)
            break
            #save image

cap.release()
cv2.destroyAllWindows()
