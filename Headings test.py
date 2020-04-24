import cv2
import numpy as np
import matplotlib.pyplot as plt

shape1 = (105, 325, 3)
shape2 = (85, 325, 3)
img = np.zeros(shape1, dtype = np.uint16)
img2 = np.zeros(shape2, dtype = np.uint16)

cv2.putText(img,'Player',(0, 75), cv2.FONT_HERSHEY_COMPLEX, 3, (255,255,255), 7)
cv2.putText(img2,'Dealer',(0, 75), cv2.FONT_HERSHEY_COMPLEX, 3, (255,255,255), 7)


layout_list = ['Start Menu', img, 'a']

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.show()

plt.imshow(img2)
plt.show()
