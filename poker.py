from deck import Deck
from card import Card

def poker():
    print("Welcome to my poker game")
    s = ""
    while s != "s":
        s = input("Enter s to start ").lower().strip()
    deck = Deck()
    player_cards = [deck.draw(),deck.draw()]
    house_cards = [deck.draw(),deck.draw()]
    table_card = [deck.draw(),deck.draw(),deck.draw()]
    print("You hand is:", show_cards(player_cards), "\nThe cards on the table are:", show_cards(table_card))



def show_cards(cards):
    card_list = ""
    for i in range(len((cards))):
        card_list += str(cards[i]) + " "
    return card_list

poker()