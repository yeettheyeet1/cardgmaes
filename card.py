class Card:

    dict = {1: "Clubs", 2: "Spades", 3: "Hearts", 4: "Diamonds", 11: "Jack", 12:"Queen", 13:"King", 14:"Ace"}
    number = 0
    symbol = 0
    value = 0

    def __init__(self,suit,number):
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







