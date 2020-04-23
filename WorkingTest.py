class Player:
    def __init__ (self, bet, c)

        self.c = 0
        self.bet = bet
        self.pool = 0
        self.cards = {}
        self.card_value = 0
        self.dd = 0
        self.splitting = 0
        self.surrender = 0
        self.win = 0
        self.turn = 0


    

    def pool_value(self, win, surrender):
        if self.surrender == 1:
            self.pool = self.pool - ((self.bet)/2)

        elif self.win == 1:
            self.pool = self.pool + self.bet

        elif self.win == 0:
            self.pool = self.pool - self.bet

    def dd_check(self):
        pass

    def double_betting(self):
        pass

    def displaying_vertical(self):
        pass

    def split_check(self):
        pass

    def __init__(self):
        pass

    def surrender (self):
        self.pool_value(surrender = 1)






bet = int(input('Enter The Betting Value'))
p = Player(bet,c )

p.c = '1K'
print(p.bet)
print(p.c)
print(p.cards)


def turn_check():
    global obj_list

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

        return l_sum

obj = turn_check()
