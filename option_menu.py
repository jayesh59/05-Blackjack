import cv2
import numpy as np
import matplotlib.pyplot as plt

shape = (210, 340, 3)
img = np.zeros(shape, dtype = np.uint16)
y = 0 
splitting = 0
dd = 0

l_options = ['1. Stay', '2. Hit', '3. Double Down', '4. Split', '5. Surrender']

for string in l_options:
    
    if string[0] == '3':

        if dd == 1:
            colour = (255,255,255)
        else:
            colour = (255,0,0)
        
        cv2.putText(img, string, (0, 24+y), cv2.FONT_HERSHEY_PLAIN, 2, colour, 2)
        y = y + 30

    elif string[0] == '4':

        if splitting == 1:
            colour = (255,255,255)
        else:
            colour = (255,0,0)
        
        cv2.putText(img, string, (0, 24+y), cv2.FONT_HERSHEY_PLAIN, 2, colour, 2)
        y = y + 30   

    else:
        cv2.putText(img, string, (0, 24+y), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
        y = y + 30    
    
    
cv2.putText(img, 'Press Your Choice...', (0, 54+y), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)

cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = np.int32(img)
plt.imshow(img)
plt.show()