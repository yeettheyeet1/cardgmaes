eclass Card:

    dict = {1: "Clubs", 2: "Spades", 3: "Hearts", 4: "Diamonds", 11: "Jack", 12:"Queen", 13:"King", 14:"Ace"}
    number = 0
    symbol = 0

    def __init__(self,symbol,number):
        if number in range(1,15):
            self.number = number
        else:
            self.number = 0
            print("bad number")

        if symbol in range(1,5):
            self.symbol = symbol
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







