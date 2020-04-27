#libraries used in this game
import random
import cv2
import matplotlib.pyplot as plt
import numpy as np

card_set = set()
len_set = 0
p = 0
d = 0
p2 = 0
obj_list = 0

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

        if obj is not None:
            self.cards = {f'{obj.l2[-1]}':obj.l2[-1]}
            self.l = []
            self.bet = 0
            self.pool = obj.pool
            self.n = 0
            self.l2 = []

    def pool_value(self):
        if self.surrender == 1:
            self.pool = self.pool - ((self.bet)/2)

        elif self.win == 1:
            self.pool = self.pool + self.bet

        elif self.win == 0:
            self.pool = self.pool - self.bet

    def split_check(self):
        if len(self.l2) > 1:
            if self.l2[-2]%100 == self.l2[-1]%100:
                if game_round != 0:
                    if self.pool > bet*2:
                        self.splitting = 1
                        return 1
                else:
                    self.splitting = 1
                    return 1
        else:
            return 0 

    def double_betting(self):
        self.bet = self.bet*2

    def displaying_vertical(self):
        pass

    def dd_check(self):
        #l = list(self.cards.values())
        if len(self.l2) == 2:
            if game_round != 0:
                if self.pool > bet*2:
                    self.dd = 1
                    return 1
            else:
                self.dd = 1
                return 1

        else:
            return 0
    
    def surrender (self):
        #self.win = 0
        self.surrender = 1
        return 0
       # end_menu(bj_check(),bust_check(),winning_check(),surrender())

def start(obj = None):
    global p, d, obj_list, card_set, len_set

    p = Player()
    d = Dealer()
    obj_list = [p,d]
    p.bet = int(input('Enter the Bet'))

    if obj is not None:
        card_set = ()
        len_set = 0
        if game_round != 0:
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
    l_sum = sum(l_values)
    a = 0

    for i in obj.cards.values():
        l.append(int(int(i)%100))

    for i in range(len(l)):
        
        if l[i] != 0 and l[i] < 10:
            pass

        elif l[i] > 9:
            l[i] = 10

        elif l[i] == 0:
            a = l.pop(i)
            i = i-1
            continue 

        l_values.append(l[i])
        
    l_sum = sum(l_values)
    if a != 0: 
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
            obj.bet = obj.bet + (obj.bet/2)
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
            return 2

        else:
            return 0

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
    obj.l_values.pop()
    obj.cards.popitem()
