import cv2
print('OpenCV version {0}'.format(cv2.__version__))
img = cv2.imread('/Users/varun/Downloads/img_42.jpg')
cv2.imshow('window',img)
cv2.waitKey()