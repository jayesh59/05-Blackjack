import cv2
import numpy as np
import matplotlib.pyplot as plt

shape = (720, 1680, 3)
img = np.zeros(shape, dtype = np.uint16)
y = 0 
splitting = 1
dd = 0

l_options = ['1. Stay', '2. Hit', '3. Double Down', '4. Split', '5. Surrender']

for string in l_options:
    
    if string[0] == '3':

        if dd == 1:
            colour = (255,255,255)
        else:
            colour = (255,0,0)
        
        cv2.putText(img, string, (600, 400+y), cv2.FONT_HERSHEY_PLAIN, 4, colour, 7)
        y= y + 67

    elif string[0] == '4':

        if splitting == 1:
            colour = (255,255,255)
        else:
            colour = (255,0,0)
        
        cv2.putText(img, string, (600, 400+y), cv2.FONT_HERSHEY_PLAIN, 4, colour, 7)
        y= y + 67    

    else:
        cv2.putText(img, string, (600, 400+y), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255), 7)
        y= y + 67    
 
cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = np.int32(img)
plt.imshow(img)
plt.show()