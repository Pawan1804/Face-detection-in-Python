import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

vd = cv2.VideoCapture(0)

while True:
    _, frame = vd.read()
    print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow("capture",frame)
    k = cv2.waitKey(1)
    if k == ord('q') :
        break

vd.release()
