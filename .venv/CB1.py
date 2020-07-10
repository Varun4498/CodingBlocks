import cv2
img = cv2.imread("/Users/varun/Desktop/ML & AI/.venv/pylogo.png")
newImg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
from matplotlib import pyplot as plt
plt.imshow(img)
#plt.imshow(newImg)
plt.show()