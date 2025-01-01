from deck import Deck
from card import Card
from appJar import gui

def poker(First):
    Gui = gui()
    if First:
        if Gui.yesNoBox("start", "Do You want to play poker?"):
            print("Welcome to my poker game")
        else:
            return
    deck = Deck()
    player_cards = [deck.draw(),deck.draw()]
    house_cards = [deck.draw(),deck.draw()]
    table_cards = [deck.draw(),deck.draw(),deck.draw()]
    print("Your hand is:", show_cards(player_cards), "\nThe table's cards are:", show_cards(table_cards))



def show_cards(cards):
    card_list = ""
    for i in range(len((cards))):
        card_list += str(cards[i]) + " "
    return card_list

##not finished
def check_Hand_Type(hand, table):
    type = {1: "high card", 2: "two of a kind", 3: "two pair", 4: "three of a kind", 5: "straight", 6: "flush", 7: "four of a kind", 8: "straight flush", 9: "royal flush"}
    suits = [0,0,0,0] #spades, clubs, hearts, diamonds
    number = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]# jack, queen, king, ace
    high = hand[0]
    type_num = 1
    for card in hand:
        suits[card.suit - 1] += 1
        number[card.number] += 1
        if card.number > high.number:
            high = card
    for card in table:
        suits[card.suit - 1] += 1
        number[card.number] += 1
        if card.number > high.number:
            high = card
    for suit in suits:
        if suit >= 5:
            flash = True
    same_high = 0
    for num in number:
        if num > same_high:
            same_high = num
    if num == 4:
        type_num = 7
    elif num == 3: 
        type_num = 4
    elif num == 2:
        type_num = 2
    return type, cards

if __name__ == "__main__":
    poker(True)
