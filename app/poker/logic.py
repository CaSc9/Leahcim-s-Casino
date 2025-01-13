import tkinter as tk
import random as rd

###
players = 4
money = 10000
bet_completed = 0
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

checked = []
all_checked = False
blind_call = True
#note to blind_call: used to check wether it's the first runthrough of calling the blinds/folding/calling the blind and raising
#also: in that mentioned first turn player 2 only has to call from the small blind to the full amount of the big blind & player 1 doesn't do anything, after that turn they play like any other

raised = False
last_completed_bet = 0
 # make status before a pAtt

set1 = False
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
def player_Attributes(players, money, bet_completed, myturn):
    for i in range(players):
        pAtt.append([])
        pAtt[i] = [i+1, "-", money, bet_completed, myturn, "-"]
    print(pAtt)
###

#1 Hände verteilen

def action_prompt(PlayerNr):
    prompt = "".join(["player ",str(PlayerNr),": call, fold, raise? "])
    return prompt

def action_prompt2(PlayerNr):
    prompt = "".join(["player ",str(PlayerNr),": fold, raise, check? "])
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
    print(table_bet)
    if (player[1] == "call" or player[1] == "raise") and player[4] == True and table_bet <= cur_money:
        if blind_call == False and player[1] == "raise":
            player[2] = cur_money - player[3]
        elif blind_call == False and player[1] != "raise":
            if player[5] == "raise" or player[5] == "call":
                player[2] = cur_money - (table_bet - player[3])
                player[3] += table_bet - player[3]
            elif player[5] != "raise":
                player[3] = table_bet
                player[2] = cur_money - table_bet
        elif blind_call == True:
            player[3] = table_bet-bigblind
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
                player[3] += amount
            amount_check = True
            print(player)
            return amount
        else:
            print("Not possible. Not enough money.")
            amount = int(input("Try again: Amount? "))

def raise_(player, table_bet, last_completed_bet):
    call(player)
    table_bet += int(r(player))
    print(table_bet)
    return table_bet

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

def check_reset(list):
    for every in list:
        if every ==  1:
            list.remove(every)
            list.append([])

def action_reset(list, this_player):
    for every in list:
        if every[5] != "raise":
            every[5] = every[1]
        if every != this_player:
            every[1] = "-"
        print(every)


################ 1. Round ##############################################################################################
print("########## ROUND 1 ###########")
create_deck()
player_Attributes(players, money, bet_completed, False)

set1 = True
deal_hands(players)
dealer_cards()

blind(players, bigblind, smallblind)

#bigblind player 1
set_bigblind(pAtt[0])

#smallblind player 2
set_smallblind(pAtt[1])


table_bet = bigblind

for i in range(players):
    checked.append([])

print(checked)

# call to full amount player 2
pAtt[1][4] = True
print("\n",Hands[1])
pAtt[1][1] = input("player 2: call, fold, raise? ")
print(pAtt[1])
if pAtt[1][1] == "call":
    set_smallblind(pAtt[1])
    checked[1] = 1
    print(checked)
elif pAtt[1][1] == "fold":
    fold(pAtt[1])
    checked[1] = 1
    print(checked)
elif pAtt[1][1] == "raise":
    raised = True
    check_reset(checked)
    print(checked)
    action_reset(pAtt, pAtt[1])
    print(pAtt)
    set_smallblind(pAtt[1])
    table_bet += int(r(pAtt[1]))
pAtt[1][4] = False

while set1 == True:
    while all_checked == False:
        if blind_call == True:
            #call players 3,4
            for i in range(2,players):
                pAtt[i][4] = True
                if pAtt[i][4] == True and all_checked == False:
                    print("\n", Hands[i])
                    pAtt[i][1] = input(action_prompt(i+1))
                    print(pAtt[i])
                    if pAtt[i][1] == "call":
                        call(pAtt[i])
                        checked[i] = 1
                        print(checked)
                    elif pAtt[i][1] == "fold":
                        fold(pAtt[i])
                        checked[i] = 1
                        print(checked)
                    elif pAtt[i][1] == "raise":
                        raised = True
                        check_reset(checked)
                        print(checked)
                        action_reset(pAtt, pAtt[i])
                        print(pAtt)
                        table_bet = raise_(pAtt[i], table_bet, last_completed_bet)
                pAtt[i][4] = False
                all_checked = all(element == 1 for element in checked)
                print(all_checked)
                if all_checked == True:
                    set1 = False
                    raised = False
            if blind_call == True:
                table_bet -= bigblind
                blind_call = False
        elif blind_call == False: # edit elif so it makes all players call the raised amount (+be sure that you can't check if you haven't called a raise)
            #call players 1,2,3,4
            for i in range(0,players):
                pAtt[i][4] = True
                print(all_checked)
                if pAtt[i][4] == True and all_checked == False:
                    if pAtt[i][1] != "raise" and raised == True: #if someone raised and it wasn't this player, he can only raise, call or fold
                        print("\n", Hands[i])
                        pAtt[i][1] = input(action_prompt(i+1))
                        print(pAtt[i])
                        if pAtt[i][1] == "call":
                            call(pAtt[i])
                            checked[i] = 1
                            print(checked)
                        elif pAtt[i][1] == "fold":
                            fold(pAtt[i])
                            checked[i] = 1
                            print(checked)
                        elif pAtt[i][1] == "raise":
                            raised = True
                            check_reset(checked)
                            print(checked)
                            action_reset(pAtt, pAtt[i])
                            print(pAtt)
                            table_bet = raise_(pAtt[i], table_bet, last_completed_bet)
                    elif pAtt[i][1] == "raise" and raised == True: #if someone raised and that was this player, then he can only raise, fold or check
                        print("\n", Hands[i])
                        pAtt[i][1] = input(action_prompt2(i + 1))
                        print(pAtt[i])
                        if pAtt[i][1] == "check":
                            checked[i] = 1
                            print(checked)
                        elif pAtt[i][1] == "fold":
                            fold(pAtt[i])
                            checked[i] = 1
                            print(checked)
                        elif pAtt[i][1] == "raise":
                            raised = True
                            check_reset(checked)
                            print(checked)
                            action_reset(pAtt, pAtt[i])
                            print(pAtt)
                            table_bet = raise_(pAtt[i], table_bet, last_completed_bet)
                    elif pAtt[i][1] != "raise" and raised == False:
                        print("\n", Hands[i])
                        pAtt[i][1] = input(action_prompt2(i + 1))
                        print(pAtt[i])
                        if pAtt[i][1] == "check":
                            checked[i] = 1
                            print(checked)
                        elif pAtt[i][1] == "fold":
                            fold(pAtt[i])
                            checked[i] = 1
                            print(checked)
                        elif pAtt[i][1] == "raise":
                            raised = True
                            check_reset(checked)
                            print(checked)
                            action_reset(pAtt, pAtt[i])
                            print(pAtt)
                            table_bet = raise_(pAtt[i], table_bet, last_completed_bet)
                pAtt[i][4] = False
                all_checked = all(element == 1 for element in checked)
                print(all_checked)
                if all_checked == True:
                    set1 = False
                    raised = False

print(table_bet)
for i in range(players):
    print(pAtt[i])

all_fold = all(element[1] == "fold" for element in pAtt)
if all_fold == True:
    print("Everyone folded, next round")
    quit()

# show first 3 dealers cards
for i in range(3):
    print("\n",DealerCards[i])

quit()


ww.mainloop()