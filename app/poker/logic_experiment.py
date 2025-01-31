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
DealerCards = []

blinds = []
bigblind = 400
smallblind = int(bigblind/2)
table_bet = 0

raised = False
called = []
all_called = False

round1 = False
round2 = False

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

def action_prompt(PlayerNr):
    prompt = "".join(["player ",str(PlayerNr),": call, fold, raise? "])
    return prompt


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
    if (player[1] == "call" or player[1] == "raise") and player[4] == True and table_bet <= cur_money:
        player[2] = cur_money - table_bet
    print(player)

def r(player):
    cur_money = player[2]
    amount = int(input("Amount? "))
    amount_check = False
    while amount_check == False :
        if amount <= cur_money:
            if player[1] == "raise" and player[4] == True:
                player[2] = cur_money - amount
            amount_check = True
            print(player)
            return amount
        else:
            print("Not possible. Not enough money.")
            amount = int(input("Try again: Amount? "))

def raise_(player, table_bet):
    call(player)
    table_bet += int(r(player))

def fold(player):
    Hands[int((player[0])-1)] = [[0, '-'], [0, '-']]
    print(player)
    print(Hands)
    print("Folded, please wait for next round.")

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

round1 = True
deal_hands(players)
dealer_cards()

blind(players, bigblind, smallblind)

#bigblind player 1
set_bigblind(pAtt[0])

#smallblind player 2
set_smallblind(pAtt[1])


table_bet = bigblind

for i in range(players-1):
    called.append([])

# call to full amount player 2
pAtt[1][4] = True
pAtt[1][1] = input("player 2: call, fold, raise? ")
print(pAtt[1])
if pAtt[1][1] == "call":
    set_smallblind(pAtt[1])
    called[0] = 1
elif pAtt[1][1] == "fold":
    fold(pAtt[1])
elif pAtt[1][1] == "raise":
    raised = True
    set_smallblind(pAtt[1])
    table_bet += int(r(pAtt[1]))
pAtt[1][4] = False

print(called)

while round1 == True:
    while raised == False and all_called == False:
        #call players 3,4
        for i in range(2,players):
            pAtt[i][4] = True
            if raised == False and pAtt[i][4] == True:
                pAtt[i][1] = input(action_prompt(i+1))
                print(pAtt[i])
                if pAtt[i][1] == "call":
                    call(pAtt[i])
                    called[i-1] = 1
                    print(called)
                elif pAtt[i][1] == "fold":
                    fold(pAtt[i])
                    called[i - 1] = 1
                    print(called)
                if pAtt[i][1] == "raise":
                    raised = True
                    raise_(pAtt[i], table_bet)
            pAtt[i][4] = False
            all_called = all(element == 1 for element in called)
            if all_called == True:
                round1 = False
        raised = False



print(table_bet)
for i in range(4):
    print(pAtt[i])


ww.mainloop()