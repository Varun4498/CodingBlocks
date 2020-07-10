import cv2
#import matplotlib.pyplot as plt

img = cv2.imread('/Users/varun/Desktop/ML & AI/.venv/img_42.jpg')
print(img.shape)
#cv2.imshow('result',img)
print(img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img, (x,y), (w,h), (color), borderWidth
cv2.rectangle(img,(20,20),(100,100),(255,0,0),5)
cv2.imshow('result',img)
