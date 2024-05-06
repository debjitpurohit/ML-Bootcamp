import cv2 #module name is cv2
cap = cv2.VideoCapture(0) # 0 is the camera index
classifier = cv2.CascadeClassifier("haarcascade_frontalface.xml")
while True:
    ret, frame = cap.read() # ret is a boolean value, frame is the image
    #if we get the ret as true means camera is working
    if ret:
        faces=classifier.detectMultiScale(frame)
        for face in faces:
            x,y,w,h = face
            debu = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 5)
        cv2.imshow("MY window", debu)

    key = cv2.waitKey(1)#if we increasae more laggy video
    if key == ord("a"): # ord is used to get the ascii value of the key
        break
cap.release()
cv2.destroyAllWindows()

# click onepicture and wait for 1000 mili sec and again take another picture and  wait for 1000 mili sec ,,thats the waitKey(1000) means