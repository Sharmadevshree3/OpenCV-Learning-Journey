import cv2

image = cv2.imread("images.png")

if image is not None:
    h ,w ,c = image.shape
    print(f"the image has loaded,\nits height is : {h},\nits width is : {w}, \nits color channel is : {c}")
else:
    print("image not loaded")