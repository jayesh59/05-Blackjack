import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

shape = (720,1680,3)
black = np.zeros(shape)
bg_copy = black.copy()
card_set = set()
len_set = 0
p = 0
d = 0
p2 = 0
obj_list = 0
game_round = 0

class Dealer:
   def __init__ (self):

        self.n = 0
        self.cards = {}
        self.card_value = 0
        self.win = 0
        self.turn = 0
        
class Player:
    def __init__ (self,obj = None):

        self.n = 0
        self.bet = 0
        self.pool = 0
        self.cards = {}
        self.card_value = 0
        self.dd = 0
        self.splitting = 0
        self.surrender = 0
        self.win = None
        self.lose = 0
        self.turn = 0
        self.l = []
        self.l_values = []
        self.l2 = []
        self.bj = 0

        if obj is not None:
            self.cards = {f'{obj.l2[-1]}':obj.l2[-1]}
            self.l = []
            self.l_values = []
            self.bet = 0
            self.win = None
            self.pool = obj.pool
            self.n = 0
            self.l2 = []
            self.surrender = 0
            self.card_value = 0
            self.dd = 0

    def pool_value(self):
        global game_round
        if game_round != 0:     
            if self.surrender == 1:
                self.pool = self.pool - ((self.bet)/2)

            elif self.win == 1:
                if self.bj == 1:
                    self.bet = (self.bet + (self.bet/2))
                self.pool = self.pool + self.bet

            elif self.win == 0:
                self.pool = self.pool - self.bet

        else:
            if self.win == 1:
                if self.bj == 1:
                    self.bet = (self.bet + (self.bet/2))
                    self.pool = self.pool + self.bet

                else:
                    self.pool = 0

    def dd_check(self):
        
        if len(self.l2) == 2:
        
            if game_round != 0:
                if self.pool > self.bet*2:
                    self.dd = 1
                    return 1
            else:

                self.dd = 1
                return 1

        else:
            return 0

    def double_betting(self):
        self.bet = self.bet*2

    def displaying_vertical(self):
        pass

    def split_check(self):
        if len(self.l2) > 1:
            if self.l2[-2]%100 == self.l2[-1]%100:
                if game_round != 0:
                    if self.pool > self.bet*2:
                        self.splitting = 1
                        return 1
                else:
                    self.splitting = 1
                    return 1
        else:
            return 0

    def surrender2 (self):
        self.surrender = 1
        return 0
       # end_menu(bj_check(),bust_check(),winning_check(),surrender())


#Functions that design and returns the layout of the 3 stages of game - Start, Gameplay, End:
def start_menu_layout():
    global black
    img = black.copy()
    y = 0

    cv2.putText(img,'BlackJack',(423, 247), cv2.FONT_HERSHEY_COMPLEX, 5, (255,255,255), 10)
    
    l_options = ['1. Start', '2. Rules', '3. Exit']

    for string in l_options:
        cv2.putText(img, string, (600, 400+y), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255), 7)
        y= y+67
        
    return img

def end_menu_layout():
    global black
    img = black.copy()
    y = 0
    #p.pool_value()
    obj = p
    
    if obj.surrender == 1 :
        cv2.putText(img,'U Surrendered!',(320, 247), cv2.FONT_HERSHEY_COMPLEX, 4, (255,255,255), 10)

    elif obj.win == 0:
        cv2.putText(img,'Defeat !!!',(423, 247), cv2.FONT_HERSHEY_COMPLEX, 5, (255,255,255), 10)

    elif obj.win == 1:
        cv2.putText(img,'Victory!!!',(423, 247), cv2.FONT_HERSHEY_COMPLEX, 5, (255,255,255), 10)
   
    l_options = ['1. Stats Status', '2. Next Round', '3. Exit']

    for string in l_options:
        cv2.putText(img, string, (600, 400+y), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255), 7)
        y= y+67

    return img

def gameplay_layout(p_turn = 0, d_turn = 0, p2_turn = 0, p_dd = 0, p_split = 0, p2_dd = 0):

     #Cards Displayin Functions:   
    def card_display_just_after_split(obj):
        card = card_layout(obj) 
        y = card_y + 10
        bg_copy[170 + y:170 + y + card_y, 20 + (obj.n*(card_x+10)):20+card_x + (obj.n*(card_x+10))] = card  
        obj.n += 1
        p.n -= 1
        bg_copy[170:170 + card_y, 20 + (obj.n*(card_x+10)):20+card_x + (obj.n*(card_x+10))] = np.zeros(card.shape)
        p.n -= 1  
               
    def card_display_player(obj):
        y = 0
        if obj == p2:
            y = card_y + 10
            
        card_distribution(obj)
        card = card_layout(obj)
        bg_copy[170 + y:170 + y + card_y, 20 + (obj.n*(card_x+10)):20+card_x + (obj.n*(card_x+10))] = card
        obj.n += 1
        
    def card_display_dealer(obj):
        card_distribution(obj)
        card = card_layout(obj)
        bg_copy[170:170+card_y, 1660-card_x - (obj.n*(card_x+10)):1660 - (obj.n*(card_x+10))] = card
        obj.n += 1
   
    #Shapes Acquiring Functions:
    #for options to show according to the split turn because options will be available to double down too.
    if p2_turn == 1:
        o = p2
    else:
        o = p

    option = option_menu_layout(o)
    stats  = stats_layout(o)
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
    if p_dd == 0:
        if d_turn == 1 and p_turn == 0 and p2_turn == 0:
            card_display_dealer(d)
            
        elif p_turn == 1 and p2_turn == 0 and d_turn == 0:
            card_display_player(p)

        elif p2_turn == 1 and p_turn == 0 and d_turn == 0:
            card_display_player(p2)

        elif p_turn == 1 and d_turn == 1 and p2_turn == 0:
            card_display_dealer(d)
            card_display_player(p)
            
        elif p_turn == 0 and p2_turn == 0 and d_turn == 0:
            pass

    elif p_dd == 1:
        card_distribution(p)
        p.card_value = cards_value(p)
        card = card_layout(p, 1)
        p.double_betting()
        c_y, c_x, _ = card.shape
        bg_copy[170:170+c_y, 20 + (p.n*(75+10)):20+c_x + (p.n*(75+10))] = card
        p.n += 1
        card_display_dealer(d)
        #d.n += 1

    if p2_dd == 1:
        card_distribution(p2)
        card = card_layout(p2, 1)
        y = card_y + 10
        c_y, c_x, _ = card.shape
        bg_copy[170 + y:170 + y + c_y, 20 + (p2.n*(75+10)):20+c_x + (p2.n*(75+10))] = card
        p.n += 1
        card_display_dealer(d)
        d.n += 1

    if p_split == 1:
        card_display_just_after_split(p2)

    return bg_copy

#Functions that design individual components of the gameplay layout:
def option_menu_layout(obj):

    shape = (210, 340, 3)
    img = np.zeros(shape)
    y = 0 
    obj.dd_check()
    obj.split_check()
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

            if obj == p2:
                colour = (0,0,255)
            elif obj.splitting == 1:
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

def card_layout(obj, p_dd = 0):
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

    y = int((img_copy.shape[0] - shapes[int((a/100))].shape[0])/2)
    x = int((img_copy.shape[1] - shapes[int((a/100))].shape[1])/2)
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

    if p_dd == 1:
        img_copy = cv2.rotate(img_copy, cv2.ROTATE_90_COUNTERCLOCKWISE)
    
    return img_copy

def stats_layout(obj):
    
    shape = (85, 305, 3)
    img = np.zeros(shape)
    y = 0 
    obj.card_value = cards_value(obj)
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

#Functions to print and call the working funtions of the game:
def displaying_starting_window():
    while True:

        frame = start_menu_layout()
        cv2.imshow('BlackJack Start', frame)

        k = cv2.waitKey(1) & 0xFF

        if k == 27 or k == ord('3'):
            return 0
            break

        elif k == ord('1'):
            start()
            break

        elif k == ord('2'):
            while True:
                frame2 = cv2.imread('Rules.jpg')
                cv2.imshow('Rules', frame2)
                k2 = cv2.waitKey(1) & 0xFF
                if k2 == 32:
                    break
            cv2.destroyWindow('Rules')         

    cv2.destroyAllWindows()

def displaying_gameplay_window():
    global game_round, p2, p, d, bg_copy
    gameplay_layout(p_turn = 1)
    gameplay_layout(p_turn = 1, d_turn = 1)
    
    def function_sequence(obj):
        
        while True:
            frame = gameplay_layout()
            cv2.imshow('Splitting Input', frame)
            k2 = cv2.waitKey(1) & 0xFF
            if k2 == ord('1'):
                break

            elif k2 == ord('2'):
                if obj == p:
                    gameplay_layout(p_turn = 1)
                    break
                else:
                    gameplay_layout(p2_turn = 1)
                    break

            elif k2 == ord('3'):
                if obj.dd == 0:
                    print('You cannot opt for this yet')
                    function_sequence(obj)    
                if obj == p:
                    gameplay_layout(p_dd = 1)
                    break                
                elif obj == p2:
                    gameplay_layout(p2_dd = 1)
                    break

            elif k2 == ord('4'):
                print('Please Just Do Not')
                function_sequence(obj)

            elif k2 == ord('5'):
                obj.surrender2()
                break
        
        cv2.destroyWindow('Splitting Input')
        return 0
    
    def winning_condition():
        global game_round

        if p.win == 0 and p2.win == 0:
            return 1

        if p.surrender == 1 or p2.surrender == 1:
            return 1
        
        if p.win == 1 or p2.win == 1:
            if p.win == 1 and p2.win == 1:
                pass
            else:
                p.bet = int(p.bet/2)
            return 1

        if bj_p == 1 and bj_p2 == 1 and bj_d == 1:
            game_round += 1
            print('It was a Tie, Begin again...')
            start(p)
            displaying_gameplay_window()
    
    while True:

        frame = gameplay_layout()
        cv2.imshow('BlackJack Gameplay', frame)
        bj_p = bj_check(p)
        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            break

        elif k == ord('1'):
            gameplay_layout(d_turn = 1)
            d.card_value = cards_value(d)
            bj_d = bj_check(d)
            if bj_d == 1:
                if bj_p == 1:
                    game_round += 1
                    print('It was a Tie, Begin again...')
                    start(p)
                    displaying_gameplay_window()
                    bg_copy = black.copy()
                else:
                    p.win = 0
                    #displaying_ending_window()

            else:
                if bj_p == 1:
                    p.win = 1
                    #displaying_ending_window()
                else:
                    pass

            w = winning_check(obj_list)
           
            if w == 1:
                gameplay_layout(d_turn = 1)
                d.card_value = cards_value(d)
                b_d = bust_check(d)
                if b_d == 0:
                    w = winning_check(obj_list)
                    if w == 1:
                        p.win = 1
                        #displaying_ending_window()

                    else:
                        p.win = 0
                        #displaying_ending_window()
                else:
                    p.win = 1
                    #displaying_ending_window()

            elif w == 2:
                continue
            
            else:
                p.win = 0
                #displaying_ending_window()

        elif k == ord('2'):
            gameplay_layout(p_turn = 1)
            p.card_value = cards_value(p)
            b_p = bust_check(p)
            bj_p = bj_check(p)

            if b_p == 1:
                p.win = 0 
                #displaying_ending_window()

            else:
                gameplay_layout(d_turn = 1)
                d.card_value = cards_value(d)
                bj_d = bj_check(d)
                if bj_d == 1:
                    if bj_p == 1:
                        game_round += 1
                        print('It was a Tie, Begin again...')
                        start(p)
                        displaying_gameplay_window()
                        bg_copy = black.copy()
                    else:
                        p.win = 0
                        #displaying_ending_window()

                else:
                    if bj_p == 1:
                        p.win = 1
                        #displaying_ending_window()
                    else:
                        pass

                w = winning_check(obj_list)
                if w == 1:
                    gameplay_layout(d_turn = 1)
                    b_d = bust_check(d)
                    if b_d == 0:
                        w = winning_check(obj_list)
                        if w == 1:
                            p.win = 1
                            #displaying_ending_window()

                        else:
                            p.win = 0
                            #displaying_ending_window()
                    else:
                        p.win = 1
                        #displaying_ending_window()

                elif w == 2:
                    continue
                
                else:
                    p.win = 0
                    #displaying_ending_window()

        elif k == ord('3'):
            if p.dd == 0:
                print('You cannot opt for this yet...')
                continue
            else:
                #p.double_betting()
                gameplay_layout(p_dd = 1)
                p.card_value = cards_value(p)
                b_p = bust_check(p)
                #b_d = bust_check(d)
                if b_p == 1:
                    p.win = 0 
                    #displaying_ending_window()

                else:
                    d.card_value = cards_value(d)
                    bj_p = bj_check(p)
                    bj_d = bj_check(d)
                 
                    if bj_d == 1:
                        if bj_p == 1:
                            game_round += 1
                            print('It was a Tie, Begin again...')
                            start(p)
                            displaying_gameplay_window()
                            bg_copy = black.copy()
                        else:
                            p.win = 0
                            #displaying_ending_window()

                    else:
                        if bj_p == 1:
                            p.win = 1
                            #displaying_ending_window()
                        else:
                            pass
                
                    w = winning_check(obj_list)
                    if w == 1:
                        gameplay_layout(d_turn = 1)
                        d.card_value = cards_value(d)
                        b_d = bust_check(d)
                        if b_d == 0:
                            w = winning_check(obj_list)
                            if w == 1:
                                p.win = 1
                                #displaying_ending_window()

                            else:
                                p.win = 0
                                #displaying_ending_window()
                        else:
                            p.win = 1
                            #displaying_ending_window()

                    elif w == 2:
                        game_round += 1
                        print('It was a Tie, Begin again...')
                        start(p)
                        displaying_gameplay_window()
                        bg_copy = black.copy()
                    
                    else:
                        p.win = 0
        
        elif k == ord('4'):
            if p.splitting == 0:
                print('You cannot opt this yet...')
                continue
            else:
                p.double_betting()
                p2 = Player(p)
                
                gameplay_layout(p_split = 1)
                gameplay_layout(p_turn = 1)
                gameplay_layout(p2_turn = 1)
                #cv2.destroyWindow('BlackJack Gameplay')
                frame = gameplay_layout()
                cv2.imshow('BlackJack Gameplay', frame)
                function_sequence(p)
                function_sequence(p2)
                gameplay_layout(d_turn = 1)
                frame = gameplay_layout()
                cv2.imshow('BlackJack Gameplay', frame)
                
                while True:
                    b_p = bust_check(p)
                    if b_p == 1:
                        p.win = 0 
                    
                    b_p2 = bust_check(p2)
                    if b_p2 == 1:
                        p2.win = 0
                    
                    bj_p = bj_check(p)
                    bj_p2 = bj_check(p2)
                    bj_d = bj_check(d)

                    o = winning_condition()
                    if o == 1:
                        break
                    if bj_d == 1:
                        p.win = 0
                        p2.win = 0
                    else:
                        if bj_p2 == 1 or bj_p == 1:
                            p.win = 1
                            p2.win = 1
                        
                    o = winning_condition()
                    if o == 1:
                        break

                    w = winning_check(obj_list)
                    if w == 1:
                        gameplay_layout(d_turn = 1)
                        frame = gameplay_layout()
                        cv2.imshow('BlackJack Gameplay', frame)
                        b_d = bust_check(d)
                        if b_d == 1:
                            p.win = 1
                        else:
                            bj_d = bj_check(d)
                            if bj_d == 1:
                                p.win = 0
                                p2.win = 0
                            else:
                                w = winning_check(obj_list)
                                if w == 1:
                                    p.win = 1
                                elif w == 2 or w == 22 or w == 21:
                                    print("It's been already a long game, let's start again please")
                                    game_round += 1
                                    start(p)
                                    displaying_gameplay_window()
                                    bg_copy = black.copy()
                                elif w == 0:
                                    p.win = 0
                                    p2.win = 0
                                
                    elif w == 0:
                        p.win = 0
                        p2.win = 0
                    elif w == 22:
                        function_sequence(p2)
                        frame = gameplay_layout()
                        cv2.imshow('BlackJack Gameplay', frame)
                        continue
                    elif w == 21:
                        function_sequence(p)
                        frame = gameplay_layout()
                        cv2.imshow('BlackJack Gameplay', frame)
                        continue
                    o = winning_condition()
                    if o == 1:
                        break                     

        elif k == ord('5'):
            p.surrender2()                

        if p.win is None and p.surrender == 0 :
            continue
        else:
            frame = gameplay_layout()
            cv2.imshow('BlackJack Gameplay', frame)
            p.pool_value()
            p.bet = 0
            game_round += 1
            displaying_ending_window()
            break

    cv2.destroyAllWindows()

def displaying_ending_window():
    global game_round, bg_copy
    flag = 0
    frame2 = 0
    #cv2.destroyWindow('BlackJack Gameplay')
    gameplay_window = 0

    while True:
        if flag == 0:
            frame = end_menu_layout()
        else:
            frame = frame2
        
        cv2.imshow('BlackJack Finish', frame)
        #img = frame.copy()
        k = cv2.waitKey(1) & 0xFF

        if k == 27 or k == ord('3'):
            break

        elif k == 32:
            flag = 0

        elif k == ord('1'):
            frame2 = stats_show_at_end()
            flag = 1

        elif k == ord('2'):
            game_round += 1
            start(p)
            bg_copy = black.copy()
            gameplay_window = 1
            break


    cv2.destroyAllWindows()
    if gameplay_window == 1:
        cv2.destroyWindow('BlackJack Gameplay')
        displaying_gameplay_window()


def start(obj = None):
    global p, d, obj_list, card_set, len_set

    p = Player()
    d = Dealer()
    obj_list = [p,d]
    p.bet = int(input('Enter the Bet'))

    if obj is not None:
        card_set = set()
        len_set = 0
        if game_round != 0:
            p.pool = obj.pool
            if p.pool > 0:
                if p.pool>p.bet:
                    print('Bet Only What You Can Afford.')
                    p.bet = int(input('Enter the Bet'))
            
        del obj

def turn_check(obj_list):
    for obj in obj_list:
        if obj.turn == 1:
            return obj

def cards_value(obj):
    l=[]
    l_values = []
    l_sum = 0
    l_sum = sum(l_values)
    a = 0
    b = 0

    for i in obj.cards.values():
        l.append(int(int(i)%100))

    for i in range(len(l)):
        
        if l[i] != 0 and l[i] < 10:
            pass

        elif l[i] > 9:
            l[i] = 10

        elif l[i] == 0:
            b = 1
            pass
                    
        l_values.append(l[i])
        
    l_sum = sum(l_values)
    if b == 1: 
        a_value = 21 - l_sum 
        if a_value-1>=0:

            if a_value-11>=0 :

                if a_value-1 > a_value-11:
                    a = 11

                else:
                    a = 1

            else:
                a = 1

        elif a_value-11>=0:
            a = 11

        else:
            a = 1

    l_sum = sum(l_values) + a

    if obj == p or obj == p2:
        obj.l = l
        obj.l_values = l_values
    
    #obj.card_value = l_sum
    return l_sum

def card_distribution(obj):
    global len_set, card_set
   
    while True:
        l = len(card_set)
        if l - len_set == 1:
            obj.cards[str(c)] = c
            break
        else:
            c_value = random.randint(0,12)
            c_suite = random.randint(0,3)*100
            c = c_value + c_suite    
            card_set.add(c)
    
    if obj == p or obj == p2:
        obj.l2 = list(obj.cards.values())
    len_set = l

def bj_check(obj):

    if obj.card_value == 21:
        
        if obj == p:
            obj.bj = 1
        return 1

    else:
        return 0

def bust_check(obj):
    
    if obj.card_value > 21:
        return 1

    else:
        return 0

def winning_check(obj_list):
    p.card_value = cards_value(p)
    d.card_value = cards_value(d)

    if len(obj_list) == 3:
        p2.card_value = cards_value(p2)
        if obj_list[2].card_value > obj_list[1].card_value or obj_list[0].card_value > obj_list[1].card_value:
            #obj_list[0].win = 1
            return 1

        elif obj_list[2].card_value == obj_list[1].card_value or obj_list[0].card_value == obj_list[1].card_value:
            if obj_list[2].card_value == obj_list[1].card_value:
                return 22
            elif obj_list[0].card_value == obj_list[1].card_value:
                return 21

        else:
            return 0

    else:
        if obj_list[0].card_value > obj_list[1].card_value:
            #obj_list[0].win = 1
            return 1
    
        elif obj_list[0].card_value == obj_list[1].card_value:
            return 2
    
        else:
            return 0

def splitting(obj):
    global obj_list
    p2 = Player(obj)
    obj_list.append(p2)
    obj.l.pop()
    obj.l2.pop()
    obj.l_values.pop()
    obj.cards.popitem()

def stats_show_at_end():
    global black
    img = black.copy()
    y = 0
    #p.pool_value()
    obj = p
    
    if obj.surrender == 1 :
        cv2.putText(img,'U Surrendered!',(320, 247), cv2.FONT_HERSHEY_COMPLEX, 4, (255,255,255), 10)

    elif obj.win == 0:
        cv2.putText(img,'Defeat !!!',(423, 247), cv2.FONT_HERSHEY_COMPLEX, 5, (255,255,255), 10)

    elif obj.win == 1:
        cv2.putText(img,'Victory!!!',(423, 247), cv2.FONT_HERSHEY_COMPLEX, 5, (255,255,255), 10)
   
    stats  = stats_layout(p)
    stats_y, stats_x, _ =  stats.shape
    img[715-stats_y:715, 5:5+stats_x] = stats

    return img

