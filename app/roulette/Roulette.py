import random
import tkinter as tk

def initiation():
    global numbers
    numbers= [
        [0, 'green', '','','']
        [1, 'red', '1', 'Odd', '1-18' ],
        [2, 'black', '1', 'Even', '1-18' ],
        [3, 'red', '1', 'Odd', '1-18' ],
        [4, 'black', '1', 'Even', '1-18' ],
        [5, 'red', '1', 'Odd', '1-18' ],
        [6, 'black', '1', 'Even', '1-18' ],
        [7, 'red', '1', 'Odd', '1-18' ],
        [8, 'black', '1', 'Even', '1-18' ],
        [9, 'red' '1', 'Odd', '1-18' ],
        [10, 'black', '1', 'Even','1-18' ],
        [11, 'black', '1', 'Odd', '1-18' ],
        [12, 'red', '1', 'Even', '1-18' ],
        [13, 'black', '2', 'Odd', '1-18' ],
        [14, 'red', '2', 'Even', '1-18' ],
        [15, 'black', '2','Odd', '1-18' ],
        [16, 'red', '2', 'Even', '1-18' ],
        [17, 'black', '2', 'Odd', '1-18' ],
        [18, 'red', '2', 'Even', '1-18' ],
        [19, 'black', '2', 'Odd', '19-36' ],
        [20, 'black', '2', 'Even', '19-36' ],
        [21, 'red', '2', 'Odd', '19-36' ],
        [22, 'black', '2', 'Even', '19-36' ],
        [23, 'red', '2', 'Odd', '19-36' ],
        [24, 'black', '2', 'Even', '19-36' ],
        [25, 'red', '3', 'Odd', '19-36' ],
        [26, 'black', '3', 'Even', '19-36' ],
        [27, 'red', '3', 'Odd', '19-36' ],
        [28, 'red', '3', 'Even', '19-36' ],
        [29, 'black', '3', 'Odd', '19-36' ],
        [30, 'red', '3', 'Even', '19-36' ],
        [31, 'black','3', 'Odd', '19-36' ],
        [32, 'red', '3', 'Even', '19-36' ],
        [33, 'black', '3', 'Odd', '19-36' ],
        [34, 'red', '3', 'Even', '19-36' ],
        [35, 'black', '3', 'Odd', '19-36' ],
        [36, 'red', '3', 'Even', '19-36' ]]


kontostand = 3000

bets = []



ww= tk.Tk()
ww.screenheight= 500
ww.screenwidth= 500
ww.title = "Roulette"


ww.mainloop()

#Todolist
#
#def betting(wette,zahl):
#    while x != 0:
#        wette = int(input("Wie viel möchtest du setzen?"))
#        zahl = int(input("Auf welche Zahl möchtest du setzen?"))
#        if zahl >36:
#            zahl = int(input("Die höchste Zahl auf die man Wetten kann ist 36. Überlege noch ein Mal"))
#        Wetten.insert(wette, zahl)
#        x = int(input("Möchten sie noch eine Wette plazieren?(1 = ja / 0 = nein)"))



def BetChoose(BetArt, Zahl):
    BetArt = int(input(
        'Auf wieviele Zahlen werden gewettet? 1 = Eine Zahl; 2 = Zwei Zahlen; 3 = Drei Zahlen; 4 = Vier Zahlen; 6 = Sechs Zahlen; 7 um Abzuschliessen'))
    while BetArt == 1 or 2 or 3 or 4 or 6 or 7:
        BetArt = int(input(
            'Auf wieviele Zahlen werden gewettet? 1 = Eine Zahl; 2 = Zwei Zahlen; 3 = Drei Zahlen; 4 = Vier Zahlen; 6 = Sechs Zahlen; 7 um Abzuschliessen'))
        if BetArt == 1:
            wettzahlen = []
            number = int(input(f"Geben Sie eine Zahl zwischen 0 und 36 ein (Sie haben {BetArt - len(wettzahlen)} verbleibende Wahlen): "))
            einsatz = int(input('Wieviel möchten sie Wetten? Sie haben',kontostand,'viel Geld übrig'))
            if number in numbers and number not in wettzahlen and einsatz <= kontostand:
                wettzahlen.append([number, einsatz])
            else:
                print("Ungültige Zahl oder bereits gewählt. Bitte versuchen Sie es erneut.")
            bets.append(wettzahlen)
            kontostand = kontostand - einsatz
        if BetArt == 2:
            wettzahlen = []
            number = int(input(
                f"Geben Sie eine Zahl zwischen 0 und 36 ein (Sie haben {BetArt - len(wettzahlen)} verbleibende Wahlen): "))
            wette = int(input('Wieviel möchten sie Wetten? Sie haben', kontostand, 'viel Geld übrig'))
            if number in numbers and number not in wettzahlen and wette >= kontostand:
                wettzahlen.append([number, wette])
            else:
                print("Ungültige Zahl oder bereits gewählt. Bitte versuchen Sie es erneut.")
            bets.append(wettzahlen)
            kontostand = kontostand - wette
        if BetArt == 3:
            bets.append()
        if BetArt == 4:
            bets.append()
        if BetArt == 6:
            bets.append()
        if BetArt == 7:
            spin()

def bet_1(zahl, einsatz):
    wettzahlen = []
    number = int(input(
        f"Geben Sie eine Zahl zwischen 0 und 36 ein (Sie haben {1 - len(wettzahlen)} verbleibende Wahlen): "))
    einsatz = int(input('Wieviel möchten sie Wetten? Sie haben', kontostand, 'viel Geld übrig'))
    if number in numbers and number not in wettzahlen and einsatz <= kontostand:
        wettzahlen.append([number, einsatz])
    else:
        print("Ungültige Zahl oder bereits gewählt. Bitte versuchen Sie es erneut.")
    bets.append(wettzahlen)
    kontostand = kontostand - einsatz

def check_bet_1(zahl, ):

def bet_2():
    

def bet_3():

def bet_4():

def bet_6():


#def EinzelBet(zahl, betrag):
    #    while zahl < 0 or zahl > 36:
    #    zahl = int(input('Auf Welche Zahl zwischen 0 und 36 wettest du?'))
    #    betrag = int(input('Welchen Betrag wettest du?'))
    #if betrag > kontostand
            #    while betrag > kontostand:
            #print('Ungenügend Geld')
        #betrag = int(input('Wieviel Wettest du?'))
    #print('Dein Kontostand ist', kontostand - betrag, '$')


def spin():
    wert = random.randint(0, 36)


def define_split(kontostand=kontostand,einsaetze =einsaetze, bets= bets) ->dict:
    '''Wette auf zwei nebeneinanderliegende definieren'''
    allowed_value = False
    count_value = 0
    allowed_einsatz = False

    for i in range 2:

        value = int(input("Auf welche Zahl soll gewettet werden?"))
        bet["type"].append(value)
        if value not in range(0, 37) or check_used_split(value, bets):
            print("Bitte gib eine Zahl zwischen 0 und 36 ein, oder eine Zahl die du noch nicht verwendet hast.")
        else:
            count_value = count_value + 1

    while allowed_einsatz == False:
        einsatz = int(input("Wieviel möchtest du setzen? Dein Kontostand beträgt " + str(kontostand - einsaetze) + "."))
        if einsatz + einsaetze > kontostand:
            print("Nicht genügend Geld vorhanden. Der Maximalbetrag ist " + str(kontostand - einsaetze) + ".")
        else:
            allowed_einsatz = True
    bet = {"type": "split",
           "value": value,
           "einsatz": einsatz}
    return bet

#1. Geld Anfordern --> Kontostand setzen
#2. Wetten setzen
#Kugel rollen lassen
#Auswerten und Gewinn auszahlen --> Kontostand aktualisieren
#Weiterspielen?

#Kontostand als einzige globale variabe




weiterspielen = True
    print("Hallo zu Roulette in Leahcim-s-Casino")
    kontostand= geld_anfordern()
    while weiterspielen:
        bets, kontostand = define_bets(kontostand=kontostand)
        wert = spin()
        gain = define_auswertung(wert=wert, bets=bets)
        kontostand+= gain
        print("Dein Kontostand beträgt:"+str(kontostand))
        weiterspielen = (str(input("Möchtest du weiterspielen? True = Ja / False = Nein")) == "True")
        if weiterspielen == True:
            geld = (str(input("Möchtest du weiteres Geld in Chips auszahlen lassen? True = Ja / False = Nein"))=="True")
            if geld == True:
                kontostand+= geld_anfordern()
            if kontostand == 0 and weiterspielen:
                print("Dein Kontostand beträgt: 0\n Zahle weiteres Geld ein!")
                kontostand += geld_anfordern()
        else:
            break