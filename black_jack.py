from deck import Deck
from appJar import gui
###from card import Card


def black_jack(First):
    Gui = gui()
    if First:
        if Gui.yesNoBox("start", "Do You want to play black jack"):
            print("Welcome to my black jack game")
        else:
            return
    deck = Deck()
    player_hand = [deck.draw(),deck.draw()]
    house_hand = [deck.draw(),deck.draw()]
    player_total,house_total = score(player_hand),score(house_hand)
    end = False
    while player_total < 21 and house_total < 21 and end == False:
        hand , total = ("Your hand is:", showHand(player_hand)), ("the total is: ", player_total)
        Gui.infoBox("show", hand + total )
        if Gui.yesNoBox("draw", "Would you like to draw a card?"):
            card = deck.draw()
            player_hand.append(card)
            card = "You draw a", card
            Gui.infoBox("Draw", card )
        else:
            end = True
        player_total = score(player_hand)
    house_hand,deck = houseLosing(house_hand,deck,player_total)
    house_total = score(house_hand)
    p_hand_Gui, p_total_Gui, h_hand_Gui, h_total_Gui = ("Your hand is:",showHand(player_hand)) , (player_total, "total" ), ("\nThe house's hand is:", showHand(house_hand)), (house_total, "total")
    Gui.infoBox("show end", p_hand_Gui + p_total_Gui + h_hand_Gui + h_total_Gui)
    #print("Your hand is:",showHand(player_hand) , player_total, "total" , "\nThe house's hand is:", showHand(house_hand), house_total, "total")
    Gui.infoBox("Conclution", Conc(player_total,house_total))
    if Gui.yesNoBox("Replay", "would you like to play again"):
        Gui.stop()
        black_jack(False)
    else:
        Gui.stop()


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
        return("Tie")
    elif player_total > 21 or house_total > 21:
        if player_total > 21 and house_total > 21:
            return("tie")
        elif player_total > 21:
            return("the house wins")
        else:
            return("You win")
    elif player_total == 21 or house_total == 21:
        if house_total == 21:
            return("the house wins")
        else:
            return("You win")
    elif player_total < house_total:
        return("the house wins")
    else:
        return("You win")

if __name__ == "__main__":
    black_jack(True)