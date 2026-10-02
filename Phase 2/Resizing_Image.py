import cv2

image = cv2.imread("images.png")

if image is None:
    print("cannot load image")

else:
    resize = cv2.resize(image, (300,300))
    cv2.imshow("original image", image)
    cv2.imshow("resized image", resize)
    cv2.waitKey(0)