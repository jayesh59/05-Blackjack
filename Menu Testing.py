import cv2
import numpy as np
import matplotlib.pyplot as plt
 
shape = (720,1680,3)
black = np.zeros(shape)

def video_format_layout(layout, obj = None):
    #global black
    while True:

        cv2.imshow(layout[0], layout[1])
        key = cv2.waitKey(1) & 0xFF 


        if layout[2] == 'a':
            if key == 27 or key == ord('3'):
                break
        
        elif layout[2] == 'b':
            if key == 27 or key == ord('3'):
                break

        elif layout[2] == 'c':
            if key == 27 or key == ord('3'):
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
        
    layout_list = ['Start Menu', img, 'a']
    return layout_list

def end_menu_layout(obj):
    global black
    img = black.copy()
    y = 0

    if obj.surrender == 1:
        cv2.putText(img,'U Surrendered!',(320, 247), cv2.FONT_HERSHEY_COMPLEX, 4, (255,255,255), 10)

    elif obj.win == 0:
        cv2.putText(img,'Defeat !!!',(423, 247), cv2.FONT_HERSHEY_COMPLEX, 5, (255,255,255), 10)

    elif obj.win == 1:
        cv2.putText(img,'Victory!!!',(423, 247), cv2.FONT_HERSHEY_COMPLEX, 5, (255,255,255), 10)
   
   l_options = ['1. Stats Status', '2. Next Round', '3. Exit']

    for string in l_options:
        cv2.putText(img, string, (600, 400+y), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255), 7)
        y= y+67

    layout_list = ['End Menu', img, 'c']
    return layout_list

def gameplay_layout(obj):
    pass

def option_menu_layout(obj):

    shape = (145, 258, 3)
    img = np.zeros(shape)
    y = 0 
    
    l_options = ['1. Stay', '2. Hit', '3. Double Down', '4. Split', '5. Surrender']

    for string in l_options:
        
        if string[0] == '3':

            if obj.dd == 1:
                colour = (255,255,255)
            else:
                colour = (255,0,0)
            
            cv2.putText(img, string, (0, 24+y), cv2.FONT_HERSHEY_PLAIN, 2, colour, 2)
            y = y + 30

        elif string[0] == '4':

            if obj.splitting == 1:
                colour = (255,255,255)
            else:
                colour = (255,0,0)
            
            cv2.putText(img, string, (0, 24+y), cv2.FONT_HERSHEY_PLAIN, 2, colour, 2)
            y = y + 30   

        else:
            cv2.putText(img, string, (0, 24+y), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
            y = y + 30    

    return img
    
def card_layout(obj):
    pass

def stats_layout(obj):
    pass




end_menu_layout()
video_format_layout()
#start_menu_layout() 