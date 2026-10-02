import cv2

image = cv2.imread("images.png")
crop = image[100:200,50:150]
cv2.imshow("original image", image)
cv2.imshow("cropped image", crop)
cv2.waitKey(0)