import cv2

image = cv2.imread("WIN_20250814_14_23_40_Pro.jpg")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("grayscale image is showing", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    save = input("do you want to save this image ? (yes/no)")
    if save == "yes":
        name = input("give me the name of the saved image: ")
        sucess = cv2.imwrite(f"{name}.png", gray)
        if sucess:
            print(f"image saved successfully as '{name}.png'")
        else:
            print("cannot save image")
    else:
        print("image not saved")

else:
    print("Image is not loaded")