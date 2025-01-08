import random

values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
signs = ["Spades", "Hearts", "Diamonds", "Clubs"]
value = []
sign = []
card = []
deck = []
my_hand = []
dealers_hand = []
bet = 1

for _ in range(4):
    for value in values:
        for sign in signs:
            card = [value, sign]
            deck.append(card)

random.shuffle(deck)

def deal(hand, number):
    for _ in range(number):
        card = deck.pop()
        hand.append(card)
    return hand

def total(hand):
    total = 0
    buchstaben = ["K", "Q", "J"]
    for card in hand:
        if card[0] in buchstaben:
            total += 10
        elif card[0] == "A":
            if total >= 11:
                total += 1
            else:
                total += 11
        else:
            total += card[0]

    return total


def round():
    global konto, double, bet
    playerIn = True
    dealerIn = True
    my_hand = []
    dealers_hand = []
    print(f"Dealer hat: {deal(dealers_hand, 1)},    X")
    #print(f"Du hast: {deal(my_hand, 2)}\nTotal: {total(my_hand)}")
    my_hand = [[5, "Hearts"], [5, "Spades"]]
    total(my_hand)
    print(my_hand)
    hit_or_stand = "1"
    if my_hand[0][0] == my_hand[1][0]:
        split = input("Split hand? (Yes = 1, No = 2)\n")
        if split == "1":
            new_hand = [my_hand.pop(0)]
            while playerIn and dealerIn:
                if total(new_hand) == 21:
                    print("Blackjack! Du hast gewonnen!")
                    konto += 2 * bet
                    break
                while hit_or_stand == "1":
                    deal(new_hand, 1)
                    print(f"Du hast: {new_hand}\nTotal: {total(new_hand)}")
                    if total(new_hand) > 21:
                        print("Bust! Du hast verloren!")
                        break
                    hit_or_stand = input("Hit: 1      Stand: 2\n")
                if total(new_hand) > 21:
                    break
                elif hit_or_stand == "2":
                    hit_or_stand = "1"
                    break
            print(new_hand)
    if total(my_hand) != 21 and split != "1":
        double = input("Double: 1   No double: 2\n")
    else:
        double = "2"
    while playerIn and dealerIn:
        if total(my_hand) == 21:
            print("Blackjack! Du hast gewonnen!")
            konto += 2 * bet
            break
        if double == "1" and split != "1":
            konto -= bet
            bet *= 2
            deal(my_hand, 1)
            if total(my_hand) > 21:
                print("Bust! Du hast verloren!")
                break
            hit_or_stand = "2"
        elif double != "1":
            hit_or_stand = input("Hit: 1      Stand: 2\n")
        while hit_or_stand == "1":
            deal(my_hand, 1)
            print(f"Du hast: {my_hand}\nTotal: {total(my_hand)}")
            if total(my_hand) > 21:
                print("Bust! Du hast verloren!")
                break
            hit_or_stand = input("Hit: 1      Stand: 2\n")
        if total(my_hand) > 21:
            break
        elif hit_or_stand == "2":
            while total(dealers_hand) <= 16:
                deal(dealers_hand, 1)
            print(f"Dealer hat: {dealers_hand}    Total: {total(dealers_hand)}")
            print(f"Du hast: {my_hand}       Total: {total(my_hand)}")
            playerIn = False
        if total(dealers_hand) > 21:
            print("Dealer busts! Du hast gewonnen!")
            konto += 2 * bet
        else:
            if total(dealers_hand) == total(my_hand):
                print("Unentschieden!")
                konto += bet
            elif total(dealers_hand) < total(my_hand):
                print("Du hast gewonnen!")
                konto += 2 * bet
            else:
                print("Du hast verloren!")
            break
        return konto


konto = 1000

while bet != "q":
    print(f"Kontostand: {konto}")
    bet = input("Bet:     (quit: q)\n")
    if bet == "q":
        print(f"\nProfit: {konto - 1000}")
        break
    elif int(bet) > konto:
        print("Zu wenig Geld auf Konto.")
        continue
    bet = int(bet)
    konto -= bet
    print(f"Kontostand: {konto}\n")
    round()
    if konto <= 0:
        print("Kontostand: 0 \nDu bist pleite!")
        break
