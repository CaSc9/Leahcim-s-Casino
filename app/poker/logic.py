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
table_bet = 0

DealerCards = []

raised = False

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
        pAtt[i] = [i+1, "-", money, bet, myturn]
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
            blinds[ct] = [ct+1, "big", True, big]
        if ct == 1:
            blinds[ct] = [ct+1, "small", True, small]
        elif ct >= 2:
            blinds[ct] = [ct+1, "", False, 0]
        ct += 1
    print(blinds)

def call(player):
    cur_money = player[2]
    if (player[1] == "call" or player[1] == "raise") and player[4] == True:
        player[2] = cur_money - table_bet
    print(player)

def r(player, table_bet):
    cur_money = player[2]
    amount = int(input("Amount? "))
    if amount <= cur_money:
        if player[1] == "raise" and player[4] == True:
            player[2] = cur_money - amount
            table_bet += amount
        print(player)
    return table_bet

def set_bigblind(pAtt):
    cur_money = pAtt[2]
    pAtt[2] = cur_money - bigblind
    print(pAtt)

def set_smallblind(pAtt):
    cur_money = pAtt[2]
    pAtt[2] = cur_money - smallblind
    print(pAtt)

################ 1. Round ##############################################################################################
print("########## ROUND 1 ###########")
create_deck()
player_Attributes(players, money, bet, False)

deal_hands(players)
dealer_cards()

blind(players, bigblind, smallblind)

#bigblind player 1
set_bigblind(pAtt[0])

#smallblind player 2
set_smallblind(pAtt[1])

#call players 3,4
for i in range(2,players):

    table_bet = bigblind

    pAtt[i][4] = True
    pAtt[i][1] = input("call, fold, raise? ")
    print(pAtt[i])
    if pAtt[i][1] == "call":
        call(pAtt[i])
    if pAtt[i][1] == "raise":
        raised = True
        call(pAtt[i])
        table_bet += int(r(pAtt[i], table_bet))

# call player 2 to full amount
pAtt[1][1] = input("call, fold, raise? ")
if pAtt[1][1] == "call":
    set_smallblind(pAtt[i])
if pAtt[1][1] == "raise":
    raised = True
    set_smallblind(pAtt[i])
    table_bet += int(r(pAtt[i], table_bet))

print(table_bet)


ww.mainloop()