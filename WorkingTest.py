#libraries used in this game
import random


card_set = ()
len_set = 0

#calsses of games
class Dealer:
    def __init__ (self):

        self.n = 0
        self.cards = {}
        self.card_value = 0
        self.win = 0
        self.turn = 0
        
class Player:
    def __init__ (self, bet):

        self.n = 0
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
                return 1

    def double_betting(self):
        bet = bet*2

    def displaying_vertical(self):
        pass

    def split_check(self):
        
        if self.l[0] == self.[1]:
            if self.pool > bet*2:
                return 1

    def __init__(self,obj):
        self.cards = {f'{obj.l[-1]}':obj.l[-1]}
        self.l = []
        self.bet = obj.bet
        self.pool = obj.pool
        #self.l.append(obj.l[-1])

    def surrender (self):
        self.pool_value(surrender = 1)
        self.win = 0
        self.surrender = 1
        return 0
       # end_menu(bj_check(),bust_check(),winning_check(),surrender())




############################################################################################################
#functions of games
def start_menu():
    pass

def option_menu():
    pass

def start(obj = None):
    
    bet = 0
    cards =0
    p = Player(bet, cards)
    d = Dealer(cards)
    obj_list = [p,d]
    p.bet = int(input('Enter the Bet'))

    if obj is not None:
        if turn_round != 0:
            p.pool = obj.pool
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
        
        if obj == p or obj == p2:
            obj.l = l
            obj.l_values = l_values
        
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
    
    len_set = l

def bj_check(obj):

    if obj.card_value == 21:
        obj.win = 1
        
        if obj == p:
            obj.bet = obj.bet + (obj.bet/2)

    else:
        return 0

def bust_check(obj):
    
    if obj.card_value > 21:
        obj.win = 0
        return 0

    else:
        return 1

def winning_check(obj_list):

    if obj_list[0].card_value > obj[1].card_value:
        obj_list[0].win = 1
        return 1

    else:
        return 0

def end_menu(p.win):
    
    p.pool_value()

    if p.win == 1:
        won()
        

    elif p.win == 0 or p.surrender == 1:
        lost()

def splitting(obj):
    p2 = Player(obj)
    card_distribution(p2)
    cards_value(p2)
    obj.l.pop()
    obj.l_values.pop()
    obj.cards.popitem()
    card_distribution(obj)
    cards_value(obj)

################################################################################################################
#loops and starting of game
turn_round = 0
obj = turn_check()
