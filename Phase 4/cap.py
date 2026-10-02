import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    if not ret :
        print("image not loaded")
        break

    cv2.imshow("webcam feed", frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        print("quit")
        break

cap.release()
cv2.destroyAllWindows()
