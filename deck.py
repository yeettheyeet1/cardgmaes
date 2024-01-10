import random
import card

class deck:

    deck =[[],[],[],[],[]]

    def __init__(self):
        self.reset()

    def show(self):
        print(self.deck)

    def reset(self):
        for i in range(1, 5):
            for ii in range(1, 15):
                self.deck[i].append(ii)

    def draw(self):
        sym = random.randint(1,5)
        num = random.randint(1,15)
        card = card(num,sym)

        return card