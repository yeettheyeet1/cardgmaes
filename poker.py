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
    type = {1: "high card", 2: "two of a kind", 3: "two pair", 4: "three of a kind", 5: "straight", 6: "flush",7: "full house", 8: "four of a kind", 9: "straight flush", 10: "royal flush"}
    suits = [0,0,0,0] #spades, clubs, hearts, diamonds
    numbers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]# jack, queen, king, ace
    type_num = 1
    highCard = [0]

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
    isflush = False
    for suit in suits:
        if suit >= 5:
            isflush = True
            flushHand = []
            flushType = suit
    
    #checks if there is a strait
    isStrait = False
    Scounter = 0, Shigh = 0
    for num in numbers:
        if num > 0:
            Scounter += 1
            if Scounter >= 5:
                Shigh = num
                isStrait = True
        else:
            Scounter = 0
    
    #checks for more the one numbers
    same_num = [[],[],[]]#pair, three of a kind, four of a kind
    amountTimes = [0,0,0] #pair, three of a kind, four of a kind.
    for num in numbers:
        if num == 4: #four of a kind
            amountTimes[2] += 1
            same_num[2].append(num)
        elif num == 3: #three of a kind
            amountTimes[1] += 1
            same_num[1].append(num)
        elif num == 2: #pair
            amountTimes[0] += 1
            same_num[0].append(num)
    
    #defines which hand is the best
    if isStrait or isflush:
        if isStrait and isflush:
            highCard = Shigh
            if highCard == 14:
                type_num = 10
            else:
                type_num = 9
        elif amountTimes[2] > 0:
            type_num = 8
        elif isflush:
            type_num = 6
        else:
            type_num = 5
    else:
        if amountTimes[2] > 0:
            type_num = 8
        elif amountTimes[1] > 0:
            type_num = 4
            if amountTimes[0] > 0:
                type_num = 7
        elif amountTimes[0] > 0:
            if amountTimes[0] > 1:
                type_num = 3
            else:
                type_num = 2
        else:
            type_num = 1
    if type_num == 1:
        for i in range(len(numbers)):
            if numbers[i] > 0:
                highCard = i + 1
    #converts the type from int[] to int
    if len(highCard) == 1:
        highCard = highCard[0]

    if type_num == 7:
        highCard = same_num[2][len(same_num[2]) - 1]
    elif type_num == 4:
        highCard = same_num[1][len(same_num[1]) - 1]
    


    return type_num, highCard

if __name__ == "__main__":
    poker(True)
