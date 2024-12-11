import tkinter as tk
import random as rd

###
players = 4
money = 1000
bet = 0
Hands = []
pAtt = []

suitC = []
suitS = []
suitD = []
suitH = []
deck = [suitC, suitS, suitD, suitH]
EdiDeck = deck

blinds = []
bigblind = 400
smallblind = int(bigblind/2)

DealerCards = []

ww = tk.Tk()
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
def player_Attributes(players, money, bet, myturn):
    for i in range(players):
        pAtt.append([])
        pAtt[i] = ["-", money, bet, myturn]
    print(pAtt)
###

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

def dealer_cards():
    for i in range(5):
        rand_suit = rd.randint(0, 3)
        rand_card = rd.randint(0, len(EdiDeck) - 1)

        DealerCards.append(EdiDeck[rand_suit][rand_card])
        EdiDeck[rand_suit].pop(rand_card)

    print(DealerCards)

# blinds
# 2 setzen gross/klein Blind
def blind(players, big, small):
    for f in range(players):
        blinds.append([])

    ct = 0
    for every in blinds:
        if ct == 0:
            blinds[ct] = ["big", True, big]
        if ct == 1:
            blinds[ct] = ["small", True, small]
        elif ct >= 2:
            blinds[ct] = ["", False, 0]
        ct += 1
    print(blinds)

def call(player):
    while player[3] == True:
        print("Hello")

### 1. Round ###
print("########## ROUND 1 ###########")
create_deck()
player_Attributes(players, money, bet, False)

deal_hands(players)
dealer_cards()

blind(players, bigblind, smallblind)

#bigblind player 1
pAtt[0][1] = money - bigblind
print(pAtt[0])

#smallblind player 2
pAtt[1][1] = money - smallblind
print(pAtt[1])

#call player 3
pAtt[2][3] = True
call(pAtt[2])
ww.mainloop()