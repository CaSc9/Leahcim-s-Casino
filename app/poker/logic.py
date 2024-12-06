import tkinter as tk
import random as rd

###
players = 4
startmoney = 200
Hands = []
pAtt = []

suitC = []
suitS = []
suitD = []
suitH = []
deck = [suitC, suitS, suitD, suitH]
EdiDeck = deck

blinds = []

DealerCards = []
###

# note für deck:
# 4 suits: clubs, spades, diamonds, hearts
# jede karte hat attribute: Zahl, Farbe, Form
# zahlen 2-12 + A

def create_deck():
    for f in deck:
        if f == suitC:
            shape = "clubs"
        elif f == suitS:
          shape = "spades"
        elif f == suitD:
            shape = "diamonds"
        elif f== suitH:
            shape = "hearts"
        for i in range(2, 13):
            f.append(i)

        for i in range(11):
            f[i-1] = [f[i-1], shape]
        f.append(["A", shape])

    print(deck)

for i in range(players):
    pAtt.append([])
    pAtt[i] = ["call", startmoney]
print(pAtt)
###
ww = tk.Tk()

#1 Hände verteilen


def deal_hands(players):
    for f in range(players):
        Hands.append([])
    for every in Hands:
        for i in range(2):
            rand_suit = rd.randint(0, 3)
            rand_card = rd.randint(0, len(EdiDeck) - 1)

            every.append(EdiDeck[rand_suit][rand_card])
            EdiDeck[rand_suit].pop(rand_card)
        print(every)
    for i in range(5):
        rand_suit = rd.randint(0, 3)
        rand_card = rd.randint(0, len(EdiDeck) - 1)

        DealerCards.append(EdiDeck[rand_suit][rand_card])
        EdiDeck[rand_suit].pop(rand_card)

    print(DealerCards)
    print(EdiDeck)

# blinds
# 2 setzen gross/klein Blind
def blind(players, strtVal):
    for f in range(players):
        blinds.append([])

    ct = 0
    for every in blinds:
        if ct == 0:
            blinds[ct] = ["big", True, strtVal]
        if ct == 1:
            blinds[ct] = ["small", True, int(strtVal/2)]
        elif ct >= 2:
            blinds[ct] = ["", False, 0]
        ct += 1
    print(blinds)

# 3 player attributes:
# fold/call/raise, money




create_deck()
deal_hands(4)
blind(4, 400)
ww.mainloop()

