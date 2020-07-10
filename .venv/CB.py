import cv2
img = cv2.imread("/Users/varun/Desktop/ML & AI/.venv/pylogo.png")
gray = cv2.imread('/Users/varun/Desktop/ML & AI/.venv/pylogo.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.imshow('gray',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()