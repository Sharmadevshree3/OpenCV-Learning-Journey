import cv2

image = cv2.imread("images.png")

if image is not None:
    sucess = cv2.imwrite("Saved_photo.png", image)
    if sucess:
        print("image saved successfully as 'Saved_photo.png'")
    else:
        print("cannot save image")
else:
    print("cannot load image")