import cv2,time

video=cv2.VideoCapture(0)
a=1

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #time.sleep(3)
    cv2.imshow("Cap_gray",gray)
    cv2.imshow("capturing", frame)
    key=cv2.waitKey(1)
    a+=1
    if key==ord("q"):
        break

print(a)
video.release()
cv2.destroyAllWindows()
