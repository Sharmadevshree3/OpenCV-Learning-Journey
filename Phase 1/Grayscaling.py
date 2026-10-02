import cv2

image = cv2.imread("images.png")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Image showing", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("cannot load image")
