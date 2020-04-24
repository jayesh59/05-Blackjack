import cv2
import numpy as np
import matplotlib.pyplot as plt

class Player:
    def __init__ (self, bet, cards):

        #self.c = 0
        self.bet = bet
        self.pool = 0
        self.cards = {}
        self.card_value = 0
        self.dd = 0
        self.splitting = 0
        self.surrender = 0
        self.win = 0
        self.lose = 0
        self.turn = 0
        self.l = []
        self.l_values = []

shape = (720, 1680, 3)
background = np.zeros(shape, dtype = np.uint16)
bg_copy = background.copy()

def option_menu_layout(obj):

    shape = (210, 340, 3)
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
    
    cv2.putText(img, 'Press Your Choice...', (0, 54+y), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)

    return img

def stats_layout(obj):
    
    shape = (85, 305, 3)
    img = np.zeros(shape)
    y = 0 
    
    l_options = {'1. Bet':f' : {obj.bet}', '2. Card Value':f' : {obj.card_value}', '3. Pool':f' : {obj.pool}'}

    for string in l_options.keys():
        cv2.putText(img, string + l_options[string], (0, 24+y), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
        y = y + 30    

    return img

def headings_badges():

    shape1 = (105, 325, 3)
    shape2 = (85, 325, 3)
    img1 = np.zeros(shape1)
    img2 = np.zeros(shape2)

    cv2.putText(img1,'Player',(0, 75), cv2.FONT_HERSHEY_COMPLEX, 3, (255,255,255), 7)
    cv2.putText(img2,'Dealer',(0, 75), cv2.FONT_HERSHEY_COMPLEX, 3, (255,255,255), 7)

    return (img1, img2)

bet = 0
cards = 0
p = Player(bet, cards)

option = option_menu_layout(p)
stats  = stats_layout(p)

headings = headings_badges()
player, dealer = headings


cv2.line(bg_copy, (840,50), (840,670), (0,255,0), 10)

bg = cv2.cvtColor(bg_copy,cv2.COLOR_BGR2RGB)

plt.imshow(bg)
plt.show()
