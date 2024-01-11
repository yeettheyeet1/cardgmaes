from deck import Deck
from card import Card

def black_jack():
    print("Welcome to my black jack game")
    s = ""
    while s != "s":
        s = input("Enter s to start ").lower().strip()
    deck = Deck()
    player_hand = [deck.draw(),deck.draw()]
    house_hand = [deck.draw(),deck.draw()]
    player_total,house_total = total(player_hand, house_hand)
    end = False
    while player_total < 21 and house_total < 21 and end == False:
            print("Your hand is:", showHand(player_hand))
            if input("If you wish to draw another card enter y ").lower().strip() == "y":
                player_hand.append(deck.draw())
                player_total,house_total = total(player_hand, house_hand)
            else:
                end = True
    print("Your hand is:",showHand(player_hand) , "\nThe house's hand is: ", showHand(house_hand))
    Conc(player_total,house_total)
    if input("Enter y if you wish to play again ").lower().strip() == "y":
        black_jack()



def showHand(hand):
    p_hand = ""
    for i in range(len(hand)):
        p_hand += str(hand[i]) + " "
    return p_hand
    



def total(player_hand, house_hand):
    p_total = 0
    h_total = 0

    for i in range(len(player_hand)):
        num = player_hand[i].number
        if num in range(1,15):
            if num < 10:
                p_total += num
            elif num < 14:
                p_total += 10
            else:
                if p_total < 11:
                    p_total += 11
                else:
                    p_total += 1

    for i in range(len(house_hand)):
        num = house_hand[i].number
        if num in range(1,15):
            if num < 10:
                h_total += num
            elif num < 14:
                h_total += 10
            else:
                if h_total < 11:
                    h_total += 11
                else:
                    h_total += 1

    return p_total,h_total

def Conc(player_total, house_total):
    if player_total == house_total:
        print("Tie")
    elif player_total > 21 or house_total > 21:
        if player_total > 21:
            print("You lose")
        else:
            print("You win")
    elif player_total == 21 or house_total == 21:
        if house_total == 21:
            print("You lose")
        else:
            print("You win")
    elif player_total < house_total:
        print("You lose")
    else:
        print("You win")


black_jack()