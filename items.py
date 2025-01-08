import random

class Card:

    dict = {1: "Clubs", 2: "Spades", 3: "Hearts", 4: "Diamonds", 11: "Jack", 12:"Queen", 13:"King", 14:"Ace"}
    number = 0
    symbol = 0
    value = 0

    def __init__(self,suit = 0,number = 0):
        if number in range(1,15):
            self.number = number
            self.value = number
            if self.number > 10:
                self.value = 10
        else:
            self.number = 0
            print("bad number")

        if suit in range(1,5):
            self.symbol = suit
        else:
            self.symbol = 0
            print("bad symbol")

    def __str__(self):
        if self.symbol != 0 and self.number != 0:
            if self.number > 10:
                return self.dict[self.number] + " of " + self.dict[self.symbol]
            else:
                return  str(self.number) + " of " + self.dict[self.symbol]
        else:
            return "This card is no good"

class Deck(Card):

    deck =[[],[],[],[]]

    def __init__(self):
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
