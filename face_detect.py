#pip install Opencv-python
#haarcascade_frontalface_default.xml


import cv2

cascade_face = cv2.CascadeClassifier('D:/Downlode File in Google/haarcascades-20220704T090335Z-001/haarcascades/haaracascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    print(ret)
    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    f = cascade_face.detectMultiScale(g, 1.3, 4)
    
    
    for (x, y, w, h) in f:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 4)
        
        
    cv2.imshow('img', img)
    k = cv2.waitkey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()    