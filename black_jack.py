from deck import Deck
from appJar import gui
###from card import Card

def black_jack(First):
    Gui = gui()
    if First:
        Gui.startSubWindow("Start",)
        if Gui.yesNoBox("start", "Do You want to play poker",parent="Start"):
            Gui.stopSubWindow()
            print("Welcome to my black jack game")
        else:
            return
    deck = Deck()
    player_hand = [deck.draw(),deck.draw()]
    house_hand = [deck.draw(),deck.draw()]
    player_total,house_total = score(player_hand),score(house_hand)
    end = False
    while player_total < 21 and house_total < 21 and end == False:
        print("Your hand is:", showHand(player_hand), "the total is: ", player_total)
        if input("If you wish to draw another card enter y ").lower().strip() == "y":
            player_hand.append(deck.draw())
        else:
            end = True
        player_total = score(player_hand)
    house_hand,deck = houseLosing(house_hand,deck,player_total)
    house_total = score(house_hand)
    print("Your hand is:",showHand(player_hand) , player_total, "total" , "\nThe house's hand is:", showHand(house_hand), house_total, "total")
    Conc(player_total,house_total)
    #Gui.startSubWindow("Replay",modal= True)
    #if Gui.yesNoBox("Replay", "would you like to play again",parent="Replay"):
    #    Gui.stopSubWindow()
    #    black_jack(False)


def showHand(hand):
    p_hand = ""
    for i in range(len(hand)):
        p_hand += str(hand[i]) + " "
    return p_hand
    
def houseLosing(house_hand, deck, player_score):
    total = score(house_hand)
    while total < player_score and total < 21 and player_score < 21:
        house_hand.append(deck.draw())
        total = score(house_hand)
    return(house_hand,deck)

def score(hand):
    total = 0
    aces=0
    for card in hand:
        if card.number == 14:
            aces +=1
        else:
            total += card.value
    for i in range(aces):
        if total < 11:
            total += 11
        else:
            total += 1
    return total



def Conc(player_total, house_total):
    if player_total == house_total:
        print("Tie")
    elif player_total > 21 or house_total > 21:
        if player_total > 21 and house_total > 21:
            print("tie")
        elif player_total > 21:
            print("the house wins")
        else:
            print("You win")
    elif player_total == 21 or house_total == 21:
        if house_total == 21:
            print("the house wins")
        else:
            print("You win")
    elif player_total < house_total:
        print("the house wins")
    else:
        print("You win")

if __name__ == "__main__":
    black_jack(True)