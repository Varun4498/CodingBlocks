import cv2

dataset = cv2.CascadeClassifier('/Users/varun/Desktop/ML & AI/.venv/haarcascade_frontalface_default.xml')
img = cv2.imread('/Users/varun/Desktop/ML & AI/.venv/img_42.jpg')
faces = dataset.detectMultiScale(img,1.3)
print(faces)
for x,y,w,h in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),5)
cv2.imwrite('result.jpg',img)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
