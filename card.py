aa
class card:

    sym_dict = {1: "Clubs", 2: "Spades", 3: "Hearts", 4: "Diamonds"}

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



    def toString(self):
        if self.symbol != 0 and self.num != 0:
            print(self.num,"of", self.symbol )
        else:
            print("This card is no good")







