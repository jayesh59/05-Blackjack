import random

class Player:
    def __init__ (self, bet, cards)

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


    

    def pool_value(self):
        if self.surrender == 1:
            self.pool = self.pool - ((self.bet)/2)

        elif self.win == 1:
            self.pool = self.pool + self.bet

        elif self.win == 0:
            self.pool = self.pool - self.bet

    def dd_check(self):
        
        if self.l[1] == self.l[-1]:
            if self.pool > bet*2:



    def double_betting(self):
        bet = bet*2

    def displaying_vertical(self):
        pass

    def split_check(self):
        pass

    def __init__(self):
        pass

    def surrender (self):
        self.pool_value(surrender = 1)
        return 0
       # end_menu(bj_check(),bust_check(),winning_check(),surrender())




############################################################################################################

def turn_check(obj_list):
    #global obj_list

    for obj in obj_list:

        if obj.turn == 1:
            return obj

def cards_value(obj):
        l=[]
        l_values = []
        
        for i in obj.cards.values():
            l.append(int(i)%100)

        for i in range(len(l)):
            
            if l[i]%100 !=0 and l[i]%100 < 10:
                l[i] = l[i]%100

            elif l[i]%100 > 9:
                l[i] = 10

            elif l[i]%100 == 0:
                a_value = 21 - l_sum 
                if a_value-1>=0:

                    if a_value-11>=0 :

                        if a_value-1 > a_value-11:
                            l[i] = 11

                        else:
                            l[i] = 1

                    else:
                        l[i] = 1

                elif a_value-11>=0:
                    l[i] = 11

                else:
                    l[i] = 1
            
            l_values.append(l[i])
            l_sum = sum(l_values)
        
        if obj == p:
            obj.l = l
            obj.l_values = l_values
        
        return l_sum

def card_distribution(obj):

    c_value = random.randint(0,13)
    c_suite =  rand.randint(0,4)*100
    c = c_value + c_suite    
    obj.cards[str(c)] = c

def bj_check(obj):
    #add the changed betting amount setting.
    if obj.card_value == 21:
        obj.win = 1
        return 1
    else:
        return 0

def bust_check(obj):
    
    if obj.card_value > 21:
        return 0

    else:
        return 1

def winning_check(obj_list):

    if obj_list[0].card_value > obj[1].card_value:
        return 1

    else:
        return 0

def end_menu():
    l =[p.win, p.b]

    if l.any(1):
        won()
        p.win = 1

    elif l.all(0):
        lost()
        p.win = 0

    p.pool_value()
#revise the end menu fucntion.
obj = turn_check()
