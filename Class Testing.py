class Player:
    def __init__ (self, bet, c1,c2,c3):

        self.bet = bet
        self.pool = 0
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.card_value = 0
        
bet = int(input('Enter The Betting Value'))
p = Player(bet, 0 ,0 ,0 )

p.c1 = '1K'
print(p.bet)
print(p.c1)

    