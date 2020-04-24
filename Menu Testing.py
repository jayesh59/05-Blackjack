import cv2
import numpy as np
import matplotlib.pyplot as plt
 
shape = (720,1680,3)
black = np.zeros(shape)
#black = cv2.cvtColor(black, cv2.COLOR_BGR2GRAY)

def frame_size():
    global black
    while True:

        cv2.imshow('Start Menu', black)

        key = cv2.waitKey(1) & 0xFF 

        if key == 27:
            break

    cv2.destroyAllWindows()

def details_coordinates():
    global black
    img = black.copy()
    
    cv2.putText(img,'BlackJack',(0, 250), cv2.FONT_HERSHEY_COMPLEX, 10, 255, 10)
    plt.imshow(img, cmap = 'gray')
    plt.show()
    

details_coordinates()    