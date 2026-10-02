import cv2
image = cv2.imread("Python.png")

if image is None:
    print("image not found")

else:
    print("image loaded successfully")
