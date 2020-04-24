import cv2
import numpy as np
import matplotlib.pyplot as plt

shape = (85, 305, 3)
img = np.zeros(shape, dtype = np.uint16)
y = 0 
bet = 43
value = 34
pool = 30

l_options = {'1. Bet':f' : {bet}', '2. Card Value':f' : {value}', '3. Pool':f' : {pool}'}

for string in l_options.keys():
    cv2.putText(img, string + l_options[string], (0, 24+y), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
    y = y + 30    

cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = np.int32(img)
plt.imshow(img)
plt.show()