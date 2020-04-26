import cv2
import numpy as np
import matplotlib.pyplot as plt
 
shape = (720,1680,3)
black = np.zeros(shape)
bg_copy = black.copy()

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

def gameplay_layout(p_turn = 0, d_turn = 0):

     #Cards Displayin Functions:   
    def card_display_player(obj):
        card_distribution(obj)
        card = card_layout(obj)
        bg_copy[170:170+card_y, 20 + (obj.n*(card_x+10)):20+card_x + (obj.n*(card_x+10))] = card
        obj.n += 1
    
    def card_display_dealer(obj):
        card_distribution(obj)
        card = card_layout(obj)
        bg_copy[170:170+card_y, 1660-card_x - (obj.n*(card_x+10)):1660 - (obj.n*(card_x+10))] = card
        obj.n += 1

    #Shapes Acquiring Functions:
    option = option_menu_layout(p)
    stats  = stats_layout(p)
    headings = headings_badges()
    player, dealer = headings    

    #Acquiring sizes :
    option_y, option_x, _ = option.shape
    stats_y, stats_x, _ =  stats.shape
    player_y, player_x, _ = player.shape
    dealer_y, dealer_x, _ = dealer.shape
    card_y, card_x, _ = (133, 75, 3)

    #line drawing:
    cv2.line(bg_copy, (840,50), (840,670), (0,255,0), 10)

    #Player Heading Insertion:
    bg_copy[20:20+player_y, 257:257+player_x] = player

    #Dealer Heading Insertion:
    bg_copy[20:20+dealer_y, 1097:1097+dealer_x] = dealer

    #Stats Menu Insertion:
    bg_copy[715-stats_y:715, 5:5+stats_x] = stats

    #Options Menu Insertion:
    bg_copy[715-option_y:715, 1675-option_x:1675] = option

    #Cards Insertion:
    if p_turn == 0 and d_turn == 1:
        card_display_dealer(d)
    
    elif p_turn == 1 and d_turn == 0:
        card_display_player(p)

    elif p_turn == 1 and d_turn == 1:
        card_display_dealer(d)
        card_display_player(p)
    
    return bg_copy

    #Resetting of the Stats and Option Menu Ground:
    bg_copy[715-option_y:715, 1675-option_x:1675] = np.zeros((210, 340, 3))
    bg_copy[715-stats_y:715, 5:5+stats_x] = np.zeros((85, 305, 3))

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
                colour = (0,0,255)
            
            cv2.putText(img, string, (0, 24+y), cv2.FONT_HERSHEY_PLAIN, 2, colour, 2)
            y = y + 30

        elif string[0] == '4':

            if obj.splitting == 1:
                colour = (255,255,255)
            else:
                colour = (0,0,255)
            
            cv2.putText(img, string, (0, 24+y), cv2.FONT_HERSHEY_PLAIN, 2, colour, 2)
            y = y + 30   

        else:
            cv2.putText(img, string, (0, 24+y), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
            y = y + 30    
    
    cv2.putText(img, 'Press Your Choice...', (0, 54+y), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)

    return img

def card_layout(obj):
    shape = (133, 75, 3)
    img_copy = np.ones(shape, dtype = np.uint16) * 255
    
    Spade_1 = cv2.imread('Spade.jpg')
    Diamond_2 = cv2.imread('Diamond.jpg')
    Club_3 = cv2.imread('Club.jpg')
    Heart_4 = cv2.imread('Heart.jpg')
    
    shapes = [Spade_1, Diamond_2, Club_3, Heart_4]

    i = 0
    for s in shapes: _, s = cv2.threshold(s, 127, 255, cv2.THRESH_BINARY); shapes[i] = s ; i += 1
    i = 0
    for s in shapes: s = cv2.resize(s, (0,0), s, 0.2, 0.2); shapes[i] = s ; i += 1

    a = list(obj.cards.values())
    a = a[-1]

    y = int((img.shape[0] - shapes[int((a/100))].shape[0])/2)
    x = int((img.shape[1] - shapes[int((a/100))].shape[1])/2)
    img_copy[y:y+shapes[int((a/100))].shape[0], x:x+shapes[int((a/100))].shape[1]] = shapes[int((a/100))]

    x = a%100
    a = int(a/100)

    if x<10 & x != 0:
        if a%2 == 0:
            cv2.putText(img_copy, str(x+1), (0, 15), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)

        else:
            cv2.putText(img_copy, str(x+1), (0, 15), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)

    else:
        if a%2 == 0:
            if x == 0:
                x='A'

            elif x == 10:
                x='J'

            elif x == 11:
                x='Q'

            elif x == 12:
                x='K'


            cv2.putText(img_copy, str(x), (0, 15), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)

        else:
            if x == 0:
                x='A'

            elif x == 10:
                x='J'

            elif x == 11:
                x='Q'

            elif x == 12:
                x='K'
                
            cv2.putText(img_copy, str(x), (0, 15), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)

    return img_copy

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

def displaying_starting_window():

    frame = start_menu_layout()
    cv2.imshow('BlackJack Start', frame)

    k = cv2.waitKey(1) & 0xFF

    if k == ord('1'):
        pass

def displaying_gameplay_window():

    frame = gameplay_layout()
    cv2.imshow('BlackJack Gameplay', frame)

    k = cv2.waitKey(1) & 0xFF

    if k == ord('1'):
        pass

def displaying_ending_window():

    frame = end_menu_layout()
    cv2.imshow('BlackJack Finish', frame)

    k = cv2.waitKey(1) & 0xFF

    if k == ord('1'):
        pass
