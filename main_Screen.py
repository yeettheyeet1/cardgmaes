from items import Deck,Card
from appJar import gui
from poker import poker
from black_jack import black_jack

def main():
    Gui.infoBox("start", "Wellcome to my card games")
    Gui.addButton("BlackJack", Card_pick)
    Gui.addButton("Poker", Card_pick)
    Gui.go()
    Gui.stop

def Card_pick(name):
    if name == "BlackJack":
        black_jack(Gui)
    elif name == "Poker":
        poker(Gui)


if __name__ == "__main__":
    Gui = gui()
    main()