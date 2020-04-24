import cv2
import numpy as np
import matplotlib.pyplot as plt

shape = (720, 1680)
img = np.zeros(shape, dtype = np.int32)
y = 0 

l_options = ['1. Start', '2. Rules', '3. Exit']

for string in l_options:
    cv2.putText(img, string, (600, 400+y), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255), 7)
    y= y+67

plt.imshow(img)
plt.show()