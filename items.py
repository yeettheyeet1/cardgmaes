import random

class Card:

    dict = {1: "Clubs", 2: "Spades", 3: "Hearts", 4: "Diamonds", 11: "Jack", 12:"Queen", 13:"King", 14:"Ace"}
    number = 0
    suit = 0
    value = 0

    #the generation function of the Card class
    def __init__(self,suit = 0,number = 0) -> None:
        if number in range(1,15):
            self.number = number
            self.value = number
            if self.number > 10:
                self.value = 10
        else:
            self.number = 0
            print("bad number")

        if suit in range(1,5):
            self.suit = suit
        else:
            self.suit = 0
            print("bad suit")

    #the toString of the Card class, returns a string
    def __str__(self) -> str:
        if self.suit != 0 and self.number != 0:
            if self.number > 10:
                return self.dict[self.number] + " of " + self.dict[self.suit]
            else:
                return  str(self.number) + " of " + self.dict[self.suit]
        else:
            return "This card is no good"

class Deck(Card):

    deck =[[],[],[],[]]

    #the generation function of the Dack class
    def __init__(self) -> None:
        for i in range(4):
            for ii in range(1,15):
                self.deck[i].append(Card(i+1,ii))
        
    #returns a card, and changes the value in the location of the card in the dack to "drawn"
    def draw(self) -> None:
        dra = True
        while dra:
            sym = random.randint(1,4)
            num = random.randint(1,14)
            card = Card(sym,num)
            dra  = self.deck[sym-1][num-1] == "drawn"
            self.deck[sym-1][num-1] = "drawn"
            
        return card
    
    #recives a card, returns if the Card is not in the deck
    def isDrawn(self,card) -> bool:
        return self.deck[[card.suit-1][card.number-1]] == "drawn"

    
    #return the toString of Deck Class
    def __str__(self) -> str:
        d = []
        for i in range(4):
            for ii in range(1,15):
                d.append(str(self.deck[i][ii-1]))
        return str(d)
