import cv2
import numpy as np
 
shape = (1680, 720)
black = np.zeros((1680,720,3))
#black = cv2.cvtColor(black, cv2.COLOR_BGR2GRAY)

while True:

    cv2.imshow('Start Menu', black)

    key = cv2.waitKey(1) & 0xFF 

    if key == 27:
        break

cv2.destroyAllWindows()