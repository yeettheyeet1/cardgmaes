from items import Deck,Card
from appJar import gui

#The poker function recives a boolean, is void.
def poker(Gui):
    type = {1: "high card", 2: "two of a kind", 3: "two pair", 4: "three of a kind", 5: "straight", 6: "flush",7: "full house", 8: "four of a kind", 9: "straight flush", 10: "royal flush"}
    if Gui.yesNoBox("start", "Do You want to play poker?"):
        print("Welcome to my poker game")
    else:
        return
    deck = Deck()
    player_cards = [deck.draw(),deck.draw()]
    house_cards = [deck.draw(),deck.draw()]
    table_cards = [deck.draw(),deck.draw(),deck.draw()]
    hands =  "Your hand is: " , player_cards , "\nThe Table's cards are: " , table_cards
    Gui.infoBox("show", hands)
    fold = not (Gui.yesNoBox("start", "Do you want to fold?"))
    while len(table_cards) < 5 and fold:
        table_cards.append(deck.draw())
        house_hand = check_Hand_Type(house_cards,table_cards)
        hands =  "Your hand is: " , player_cards , "\nThe Table's cards are: " , table_cards
        Gui.infoBox("show", hands)
        if len(table_cards) < 5:
            fold = not (Gui.yesNoBox("start", "Do you want to fold?"))
    player_hand = check_Hand_Type(player_cards,table_cards)
    house_hand = check_Hand_Type(house_cards,table_cards)
    hands = "player: ", player_hand, " House: " , house_hand,"\n", check_Win(player_hand,house_hand)
    Gui.infoBox("show", hands)        
    if Gui.yesNoBox("Replay", "would you like to play again"):
        Gui.stop()
        poker(Gui)
    else:
        return


# recives an arrey of cards class, returns a string of their information.
def show_cards(cards) -> str:
    card_list = ""
    for i in range(len((cards))):
        card_list += str(cards[i]) + " "
    return card_list

#checks what type the hand is and returns the high card
def check_Hand_Type(hand, table):
    suits = [0,0,0,0] #spades, clubs, hearts, diamonds
    numbers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]# jack, queen, king, ace
    hand_type_num = 1
    highCard = 0

    #adds the cards data for the suits and numbers arreys
    for card in hand:
        suits[card.suit - 1] += 1
        numbers[card.number] += 1
        #if card.numbers > high.numbers:
        #    high = card
    for card in table:
        suits[card.suit - 1] += 1
        numbers[card.number] += 1
        #if card.numbers > high.numbers:
        #    high = card

    #checks if there is a flush
    isflush = False
    fHigh = 0
    for suit in suits:
        if suit >= 5:
            isflush = True
            flushType = suit
    if isflush:
        for card in hand:
            if card.suit == flushType:
                if card.number > fHigh:
                    fHigh = card.number
    
    #checks if there is a straight
    isStraight = False
    Scounter = 0
    SHigh = 0
    ncounter = 0
    for num in numbers:
        if num > 0:
            Scounter += 1
            if Scounter >= 5:
                SHigh = ncounter
                isStraight = True
        else:
            Scounter = 0
        ncounter += 1
    
    #checks for more then one numbers
    same_num = [[],[],[]]#pair, three of a kind, four of a kind
    amountTimes = [0,0,0] #pair, three of a kind, four of a kind.
    ncounter = 0
    for num in numbers:
        if num == 4: #four of a kind
            amountTimes[2] += 1
            same_num[2].append(ncounter)
        elif num == 3: #three of a kind
            amountTimes[1] += 1
            same_num[1].append(ncounter)
        elif num == 2: #pair
            amountTimes[0] += 1
            same_num[0].append(ncounter)
        ncounter += 1
    
    #defines which hand is the best
    if isStraight and isflush:
        if fHigh == SHigh:
            highCard = SHigh
            if highCard == 14:
                type_num = 10
            else:
                type_num = 9
    else:
        if amountTimes[2] > 0:
            type_num = 8
            highCard = same_num[2][same_num[2].length - 1]
        elif (amountTimes[1] > 0 and amountTimes[0] > 0):
            type_num = 7
            highCard = same_num[1][same_num[1].length - 1]
        elif isflush:
            type_num = 6
            highCard = fHigh
        elif isStraight:
            type_num = 5
            highCard = SHigh
        elif amountTimes[1] > 0:
            type_num = 4
            highCard = same_num[1][len(same_num[1]) - 1]
        elif amountTimes[0] > 0:
            if amountTimes[0] > 1:
                type_num = 3
            else:
                type_num = 2
            highCard = same_num[0][len(same_num[0]) - 1]
        else:
            type_num = 1
    if type_num == 1:
        for i in range(len(numbers)):
            if numbers[i] > 0:
                highCard = i + 1
    return type_num, highCard

def check_Win(player_score, house_score):
    winner = "House Wins"
    if player_score[0] > house_score[0]:
        winner = "Player Wins"
    elif player_score[0] == house_score[0]:
        if player_score[1] > house_score[1]:
            winner = "Player Wins"
        elif player_score[1] == house_score[1]:
            winner = "Tie"
    return winner

if __name__ == "__main__":
    poker(True)
