import cv2

image = cv2.imread("images.png")

if image is None:
    print("img not loaded")

else:
    print("image loaded successfully")

    cv2.putText(image, "hiiiiiiii", (50,150), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1.2,(0.255,255), 4)
    cv2.imshow("text image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows