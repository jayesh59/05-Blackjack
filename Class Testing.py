class Player:
    def __init__ (self, bet, c):

        self.bet = bet
        self.pool = 0
        self.c = c

        self.card_value = 0
        
bet = int(input('Enter The Betting Value'))
p = Player(bet, 0 )

def test(obj):

    obj.c = '1k'
    return obj.c

p.c = test(p)
print(p.c)