import random
from card import Card

class Deck:

    deck =[[],[],[],[]]

    def __init__(self):
        self.reset()

    def reset(self):
        for i in range(4):
            for ii in range(1,15):
                self.deck[i].append(Card(i+1,ii))

    def draw(self):
        dra = True
        while dra:
            sym = random.randint(1,4)
            num = random.randint(1,14)
            card = Card(sym,num)
            dra  = self.deck[sym-1][num-1] == "drawn"
            self.deck[sym-1][num-1] = "drawn"
            
        return card
    
    def isDrawn(self,card):
        return self.deck[[card.symbol-1][card.number-1]] == "drawn"

    
    
    def __str__(self):
        d = []
        for i in range(4):
            for ii in range(1,15):
                d.append(str(self.deck[i][ii-1]))
        return str(d)
