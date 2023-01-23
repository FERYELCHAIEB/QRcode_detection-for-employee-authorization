import cv2
import numpy as np
from pyzbar.pyzbar import decode 

#img=cv2.imread('cvisite.png')
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

with open('IDlist.txt') as file:
    dataList = file.read().splitlines()

while True:
    success,img=cap.read()
    #get information about position weight and height
    for barcode in decode(img):
        
        myData=barcode.data.decode('utf-8')
        #print(myData)
        if myData in dataList:
           res='authorized'
           color=(0,255,0)
        else:
            res='unauthorized'
            color=(0,0,255)
        pts=np.array([barcode.polygon],np.int32)
        pts=pts.reshape(-1,1,2)
        cv2.polylines(img,[pts],True,color,5)
        pts2=barcode.rect
        cv2.putText(img,res,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_PLAIN,0.9,color,2)
    cv2.imshow('QRcode',img)
    if(cv2.waitKey(1)==27):
        break

cv2.destroyAllWindows()