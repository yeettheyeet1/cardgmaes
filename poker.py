from items import Deck,Card
from appJar import gui

#The poker function recives a boolean, is void.
def poker(First = False):
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


# recives an arrey of cards class, returns a string of their information.
def show_cards(cards = [Card(),Card()]) -> str:
    card_list = ""
    for i in range(len((cards))):
        card_list += str(cards[i]) + " "
    return card_list

##not finished
def check_Hand_Type(hand, table):
    type = {1: "high card", 2: "two of a kind", 3: "two pair", 4: "three of a kind", 5: "straight", 6: "flush", 7: "four of a kind", 8: "straight flush", 9: "royal flush"}
    suits = [0,0,0,0] #spades, clubs, hearts, diamonds
    numbers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]# jack, queen, king, ace
    high = hand[0]
    type_num = 1

    #adds the cards data for the suits and numbers arreys
    for card in hand:
        suits[card.suit - 1] += 1
        numbers[card.numbers] += 1
        if card.numbers > high.numbers:
            high = card
    for card in table:
        suits[card.suit - 1] += 1
        numbers[card.numbers] += 1
        if card.numbers > high.numbers:
            high = card

    #checks if there is a flash
    for suit in suits:
        if suit >= 5:
            flash = True
    

    same_high = 0
    for num in numbers:
        if num > same_high:
            same_high = num
    if num == 4:
        type_num = 7
    elif num == 3: 
        type_num = 4
    elif num == 2:
        type_num = 2


    return type, #cards

if __name__ == "__main__":
    poker(True)
