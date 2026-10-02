import cv2

image = cv2.imread("meeeee.jpg")

if image is None:
    print("cannot load image")

else:
    blurred = cv2.GaussianBlur(image, (7,7),5)
    cv2.imshow("blur image",blurred)
    cv2.imshow("original",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()