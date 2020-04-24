import cv2
import numpy as np
import matplotlib.pyplot as plt
 
shape = (720,1680,3)
black = np.zeros(shape)#dtype =  np.int32)
#black = cv2.cvtColor(black, cv2.COLOR_BGR2GRAY)

def video_format_layout():
    #global black
    while True:

        black_img = start_menu_layout() 
        #print(black_img.shape)
        #black_img = np.float(black_img)
        cv2.imshow('Start Menu', black_img)

        key = cv2.waitKey(1) & 0xFF 

        if key == 27:
            break

    cv2.destroyAllWindows()

def start_menu_layout():
    global black
    img = black.copy()
    y = 0

    cv2.putText(img,'BlackJack',(423, 247), cv2.FONT_HERSHEY_COMPLEX, 5, (255,255,255), 10)
    
    l_options = ['1. Start', '2. Rules', '3. Exit']

    for string in l_options:
        cv2.putText(img, string, (600, 400+y), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255), 7)
        y= y+67
    print(img.shape)
    return img

video_format_layout()   
#start_menu_layout() 