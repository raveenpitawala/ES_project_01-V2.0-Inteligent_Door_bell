import cv2
import time
from datetime import datetime


video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("Trainer.yml")  #model path

name_list = ["", "family","family"]  # curruntly 2 members

last_serial = None
last_announcement_time = time.time()

announcement_interval = 10

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        serial, conf = recognizer.predict(gray[y:y+h, x:x+w])

        if conf < 50:
            name = name_list[serial]
            text = f"{name}"
        else:
            text = "not family"

        cv2.rectangle(frame, (x, y - 40), (x + w, y), (0, 0, 0), -1)
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        current_time = time.time()

        # Check if the face has changed or 30 seconds have passed since the last announcement
        if serial != last_serial or (current_time - last_announcement_time) > announcement_interval:
            last_serial = serial
            last_announcement_time = current_time

    frame = cv2.resize(frame, (640, 480))
    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)

    if k == ord("q"):
        break

video.release()
cv2.destroyAllWindows() 