import cv2

image = cv2.imread("images.png")

if image is None:
    print("not loaded")

else:
    print("image loaded succesfully")

    pt1 = (50,100)
    pt2 = (300,100)

    color = (255,0,0)
    thickness = 4

    cv2.line(image,pt1,pt2,color,thickness)
    cv2.imshow("lined image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()