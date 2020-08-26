import cv2

cap = cv2.VideoCapture(0)

window_name = 'bg'

while cap.isOpened():
    check, bg = cap.read()
    if check:
        cv2.imshow("window_name", bg)

        if cv2.waitKey(5) == ord('s'):
            cv2.imwrite("final1.jpg", bg)
            break

cap.release()
cv2.destroyAllWindows()


