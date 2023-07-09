import cv2

def snapshot():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    img_counter = 0
    n=0
    while(n<2):
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)
        img_name = "pics_from_test\\opencv_frame_{}.png".format(img_counter)
        img_counter += 1
        cv2.imwrite(img_name, frame)
       # print("{} written!".format(img_name))
        n=n+1
    cam.release()
    cv2.destroyAllWindows()


