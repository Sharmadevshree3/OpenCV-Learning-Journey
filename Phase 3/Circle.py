import cv2

image = cv2.imread("images.png")

if image is None:
    print("not loaded")

else:
    print("image loaded succesfully")

    cv2.circle(image,(150,150),50,(0,255,0),-1)
    cv2.imshow("circle image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()