import cv2

image = cv2.imread("meeeee.jpg", cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(image, 50,150)

print(image is None)

cv2.imshow("flower", image)
cv2.imshow("canny",edges)
cv2.waitKey(0)

cv2.destroyAllWindows()