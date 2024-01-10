class Card:

    dict = {1: "Clubs", 2: "Spades", 3: "Hearts", 4: "Diamonds", 11: "Jack", 12:"Queen", 13:"King", 14:"Ace"}

    def __init__(self,num,symbol):
        if num in range(1,15):
            self.num = num
        else:
            self.num = 0
            print("bad number")

        if symbol in range(1,5):
            self.symbol = symbol
        else:
            self.symbol = 0
            print("bad symbol")



    def __str__(self):
        if self.symbol != 0 and self.num != 0:
            if self.num > 10:
                return self.dict[self.num] + " of " + self.dict[self.symbol]
            else:
                return  str(self.num) + " of " + self.dict[self.symbol]
        else:
            return "This card is no good"







