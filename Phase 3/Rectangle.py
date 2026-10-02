import cv2

image = cv2.imread("images.png")

if image is None:
    print("not loaded")

else:
    print("image loaded succesfully")

    pt1 = (50,50)
    pt2 = (250,200)

    color = (0,0,255)
    thickness = 4

    cv2.rectangle(image,pt1,pt2,color,thickness)
    cv2.imshow("rectangle image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()