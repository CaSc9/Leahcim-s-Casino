import random
import tkinter as tk
from tkinter import ttk




global numbers
numbers= [
    [0, 'green', '', '', ''],
    [1, 'red', '1', 'Odd', '1-18'],
    [2, 'black', '1', 'Even', '1-18'],
    [3, 'red', '1', 'Odd', '1-18'],
    [4, 'black', '1', 'Even', '1-18'],
    [5, 'red', '1', 'Odd', '1-18'],
    [6, 'black', '1', 'Even', '1-18'],
    [7, 'red', '1', 'Odd', '1-18'],
    [8, 'black', '1', 'Even', '1-18'],
    [9, 'red' '1', 'Odd', '1-18'],
    [10, 'black', '1', 'Even', '1-18'],
    [11, 'black', '1', 'Odd', '1-18'],
    [12, 'red', '1', 'Even', '1-18'],
    [13, 'black', '2', 'Odd', '1-18'],
    [14, 'red', '2', 'Even', '1-18'],
    [15, 'black', '2', 'Odd', '1-18'],
    [16, 'red', '2', 'Even', '1-18'],
    [17, 'black', '2', 'Odd', '1-18'],
    [18, 'red', '2', 'Even', '1-18'],
    [19, 'black', '2', 'Odd', '19-36'],
    [20, 'black', '2', 'Even', '19-36'],
    [21, 'red', '2', 'Odd', '19-36'],
    [22, 'black', '2', 'Even', '19-36'],
    [23, 'red', '2', 'Odd', '19-36'],
    [24, 'black', '2', 'Even', '19-36'],
    [25, 'red', '3', 'Odd', '19-36'],
    [26, 'black', '3', 'Even', '19-36'],
    [27, 'red', '3', 'Odd', '19-36'],
    [28, 'red', '3', 'Even', '19-36'],
    [29, 'black', '3', 'Odd', '19-36'],
    [30, 'red', '3', 'Even', '19-36'],
    [31, 'black', '3', 'Odd', '19-36'],
    [32, 'red', '3', 'Even', '19-36'],
    [33, 'black', '3', 'Odd', '19-36'],
    [34, 'red', '3', 'Even', '19-36'],
    [35, 'black', '3', 'Odd', '19-36'],
    [36, 'red', '3', 'Even', '19-36']]

global bet_types
bet_types =['full number',
            'split',
            'street',
            'corner',
            'six line',
            'odd/even',
            'red/black',
            'dozens',
            'columns',
            'high/low']


def geld_anfordern()-> int:
    kontostand = int(input("Wie viel Geld möchtest du in Chips ausgezahlt bekommen?"))
    return kontostand


def define_bets(kontostand: int ) -> (list, int):
    '''Erstellt eine Liste in der die Wetten gespeichert werden und später wieder aufgerufen werden können'''
    bets = []

    weitere_wetten = True
    while weitere_wetten:
        allowed_bet_type = False
        while not allowed_bet_type:
            type = str(input("Welche Art von Wette soll getätigt werden?\n Zur Auswahl stehen 'full number', 'split', 'street','corner','six line', 'odd/even', 'red/black','dozens', 'columns','high/low'  "))
            if type not in bet_types:
                print("Unbekannte Art zu wetten. Versuche noch einmal.")
            else:
                allowed_bet_type = True
        if type == 'full number':
            bet = define_full_number(kontostand=kontostand, bets= bets)
            kontostand -= bet["einsatz"]
            bets.append(bet)
        if type == 'split':
            bet = define_split(kontostand=kontostand, bets= bets)
            kontostand -= bet["einsatz"]
            bets.append(bet)
        if type == 'street':
            bet = define_street(kontostand=kontostand, bets= bets)
            kontostand -= bet["einsatz"]
            bets.append(bet)
        if type == 'corner':
            bet = define_corner(kontostand=kontostand,  bets=bets)
            kontostand -= bet["einsatz"]
            bets.append(bet)
        if type == 'six line':
            bet = define_six_line(kontostand=kontostand, bets=bets)
            kontostand -= bet["einsatz"]
            bets.append(bet)
        if type == 'odd/even':
            bet = define_odd_even(kontostand=kontostand,  bets=bets)
            kontostand -= bet["einsatz"]
            bets.append(bet)
        if type == 'red/black':
            bet = define_red_black(kontostand=kontostand,  bets=bets)
            kontostand -= bet["einsatz"]
            bets.append(bet)
        if type == 'dozens':
            bet = define_dozens(kontostand=kontostand, bets=bets)
            kontostand -= bet["einsatz"]
            bets.append(bet)
        if type == 'columns':
            bet = define_columns(kontostand=kontostand, bets=bets)
            kontostand -= bet["einsatz"]
            bets.append(bet)
        if type == 'high/low':
            bet = define_high_low(kontostand=kontostand)
            kontostand -= bet["einsatz"]
            bets.append(bet)
        print("Dein aktueller Kontostand beträgt: "+str(kontostand))
        weitere_wetten = (str(input("Möchtest du eine weitere Wette platzieren? 'Ja' / 'Nein'")) == "Ja")
        if kontostand == 0:
            weitere_wetten = False
    return bets, kontostand






def define_full_number(kontostand : int,  bets: list) -> dict:
    '''Wette auf eine einzelne Zahl definieren'''
    allowed_value = False
    allowed_einsatz = False
    while allowed_value == False:
        value = int(input("Auf welche Zahl soll gewettet werden?"))
        if value not in range(0, 37) :
            print("Bitte gib eine Zahl zwischen 0 und 36 ein.")
        else:
            allowed_value = True
    while allowed_einsatz == False:
        einsatz = int(input("Wieviel möchtest du setzen? Dein Kontostand beträgt "+str(kontostand)+"."))
        if einsatz > kontostand or einsatz < 0:
            print("Nicht genügend Geld vorhanden. Der Maximalbetrag ist "+ str(kontostand)+".")
        else:
            allowed_einsatz = True
    bet ={"type": "full number",
          "value": value,
          "einsatz": einsatz}
    return bet




def define_split(kontostand: int, bets: list) -> dict:
    '''Wette auf zwei nebeneinanderliegende definieren'''
    allowed_value = False
    allowed_einsatz = False
    values = []  # Liste für die beiden Werte
    count_value = 0  # Zähler für die eingegebenen Werte

    # Schleife für die Eingabe von zwei Werten
    while not allowed_value:
        value = int(input("Gib die" + str(count_value + 1) +"-te Zahl ein. (0-36) "))
        if value not in range(0, 37) :
            print("Bitte gib eine Zahl zwischen 0 und 36 ein.")
        else:
            values.append(value)  # Wert zur Liste hinzufügen
            count_value += 1  # Zähler erhöhen
            if count_value == 2:
                allowed_value = true_split(values)
                if not allowed_value:
                    print("Bitte gib ein erlaubtes Zahlenpaar ein. Die Zahlen müssen auf dem Spielfeld nebeneinander liegen.")
                    values = []
                    count_value = 0
    while not allowed_einsatz:
        einsatz = int(input("Wieviel möchtest du setzen? Dein Kontostand beträgt " + str(kontostand) + ". "))
        if einsatz > kontostand or einsatz < 0:
            print("Nicht genügend Geld vorhanden. Der Maximalbetrag ist " + str(kontostand) + ".")
        else:
            allowed_einsatz = True
    bet = {
        "type": "split",
        "value": values,  # Liste mit beiden Werten
        "einsatz": einsatz
    }
    return bet


def true_split(values: list) -> bool:
    v_1 = values[0]
    v_2 = values[1]
    print(values)
    if (v_1 % 3) == 0: #v_1 ist in der ersten Zeile
        if v_1 in [1,2,3]: # v_1 in der ersten Spalte
            allowed_values = (v_2 in [0,2,6])
        elif v_1 in [34,35,36] : # v_1 in der letzten Spalte
            allowed_values = (v_2 in [33,35])
        elif v_1 == 0:
            allowed_values = (v_2 in [1,3,5])
        else: #in einer der mittleren Spalten
            allowed_values = (v_2 == v_1 -1 or abs(v_2 - v_1) == 3)
    elif (v_1 -1 % 3) == 0: #v_1 in der untersten Zeile
        if v_1 in [1,2,3]: # v_1 in der ersten Spalte
            allowed_values = (v_2 in [0,2,4])
        elif v_1 in [34,35,36] : # v_1 in der letzten Spalte
            allowed_values = (v_2 in [31,35])
        else: #in einer der mittleren Spalten
            allowed_values = (v_2 == v_1 + 1 or abs(v_2 - v_1) == 3)
    else:# v_1 liegt in der mittleren Zeile
        if v_1 in [1,2,3]: # v_1 in der ersten Spalte
            allowed_values = (v_2 in [0,1,3,5])
        elif v_1 in [34,35,36] : # v_1 in der letzten Spalte
            allowed_values = (v_2 in [33,34,36])
        else: #in einer der mittleren Spalten
            allowed_values = (abs(v_2- v_1) == 1 or abs(v_2 - v_1) == 3)
    return allowed_values



def define_street(kontostand: int, bets: list) -> dict:
    '''Wette auf zwei nebeneinanderliegende definieren'''
    allowed_value = False
    allowed_einsatz = False
    values = []  # Liste für die Werte
    count_value = 0  # Zähler für die eingegebenen Werte

    # Schleife für die Eingabe von mehreren Werten
    while allowed_value == False and count_value < 3:
        value = int(input("Gib die" + str(count_value + 1) +"-te Zahl ein. (0-36) "))
        if value not in range(0, 37) :
            print("Bitte gib eine Zahl zwischen 0 und 36 ein.")
        else:
            values.append(value)  # Wert zur Liste hinzufügen
            count_value += 1  # Zähler erhöhen
            if count_value == 3:
                allowed_value = true_street(values)
                if not allowed_value:
                    print("Bitte gib eine erlaubte Street ein. Die Zahlen müssen auf dem Spielfeld nebeneinander liegen.")
                    values = []
                    count_value = 0
    while allowed_einsatz == False:
        einsatz = int(input("Wieviel möchtest du setzen? Dein Kontostand beträgt " + str(kontostand) + ". "))
        if einsatz > kontostand or einsatz < 0:
            print("Nicht genügend Geld vorhanden. Der Maximalbetrag ist " + str(kontostand) + ".")
        else:
            allowed_einsatz = True
    bet = {
        "type": "split",
        "value": values,  # Liste mit den Werten
        "einsatz": einsatz
    }
    return bet

def true_street(values: list) -> bool:
    values_sorted = sorted(values)
    v_1 = values_sorted[0]
    v_2 = values_sorted[1]
    v_3 = values_sorted[2]
    allowed_value = ((v_2-v_1)==1 and (v_3-v_2)==1 and (v_3 % 3)==0)
    return allowed_value

def define_corner(kontostand: int, bets: list) -> dict:
    '''Wette auf zwei nebeneinanderliegende definieren'''
    allowed_value = False
    allowed_einsatz = False
    values = []  # Liste für die  Werte
    count_value = 0  # Zähler für die eingegebenen Werte

    # Schleife für die Eingabe von mehreren Werten
    while allowed_value == False and count_value < 4:
        value = int(input("Gib die" + str(count_value + 1) +"-te Zahl ein. (0-36) "))
        if value not in range(0, 37) :
            print("Bitte gib eine Zahl zwischen 0 und 36 ein.")
        else:
            values.append(value)  # Wert zur Liste hinzufügen
            count_value += 1  # Zähler erhöhen
            if count_value == 4:
                allowed_value = true_corner(values)
                if not allowed_value:
                    print("Bitte gib eine erlaubte Corner-Zahlenkombination ein. Die Zahlen müssen auf dem Spielfeld nebeneinander liegen.")
                    values = []
                    count_value = 0
    while allowed_einsatz == False:
        einsatz = int(input("Wieviel möchtest du setzen? Dein Kontostand beträgt " + str(kontostand) + ". "))
        if einsatz > kontostand or einsatz < 0:
            print("Nicht genügend Geld vorhanden. Der Maximalbetrag ist " + str(kontostand) + ".")
        else:
            allowed_einsatz = True
    bet = {
        "type": "split",
        "value": values,  # Liste mit den Werten
        "einsatz": einsatz
    }
    return bet

def true_corner(values: list) -> bool:
    values_sorted = sorted(values) #zahlen aufsteigend ordnen
    v_1 = values_sorted[0]
    v_2 = values_sorted[1]
    v_3 = values_sorted[2]
    v_4 = values_sorted[3]
    allowed_values = ((v_2 - v_1) ==1 and (v_4 - v_3) == 1 and (v_3 -v_1) == 3 and (v_4 - v_2) == 3) #bedingungen erfüllen mit Abstand
    return allowed_values


def define_six_line(kontostand: int, bets: list) -> dict:
    '''Wette auf zwei nebeneinanderliegende definieren'''
    allowed_value = False
    allowed_einsatz = False
    values = []  # Liste für die Werte
    count_value = 0  # Zähler für die eingegebenen Werte

    # Schleife für die Eingabe von mehreren Werten
    while not allowed_value:
        value = int(input("Gib die" + str(count_value + 1) +"-te Zahl ein. (0-36) "))
        if value not in range(0, 37) :
            print("Bitte gib eine Zahl zwischen 0 und 36 ein.")
        else:
            values.append(value)  # Wert zur Liste hinzufügen
            count_value += 1  # Zähler erhöhen
            if count_value == 6:
                allowed_value = true_six_line(values)
                if not allowed_value:
                    print("Bitte gib eine erlaubte six Line ein.")
                    values = []
                    count_value = 0
    while allowed_einsatz == False:
        einsatz = int(input("Wieviel möchtest du setzen? Dein Kontostand beträgt " + str(kontostand) + ". "))
        if einsatz > kontostand or einsatz < 0:
            print("Nicht genügend Geld vorhanden. Der Maximalbetrag ist " + str(kontostand) + ".")
        else:
            allowed_einsatz = True
    bet = {
        "type": "split",
        "value": values,  # Liste mit den Werten
        "einsatz": einsatz
    }
    return bet


def true_six_line(values: list) -> bool:
    values_sorted = sorted(values)
    v_1 = values_sorted[:3]
    v_2 = values_sorted[3:]
    allowed_values = (true_street(v_1) and true_street(v_2) and abs(v_1[0] - v_2[0])== 3)
    return allowed_values


def define_odd_even(kontostand:int, bets : list) -> dict:
    '''Wette auf gerade oder ungerade definieren'''
    allowed_value = False
    allowed_einsatz = False
    x = ['Odd', 'Even']
    while allowed_value == False:
        value = str(input("Soll auf 'Even' oder 'Odd' gewettet werden?"))
        if value not in x :
            print("Bitte gib entweder 'Even' oder 'Odd' ein, oder die Art, die noch nicht verwendet wurde.")
        else:
            allowed_value = True
    while allowed_einsatz == False:
        einsatz = int(input("Wieviel möchtest du setzen? Dein Kontostand beträgt " + str(kontostand) + "."))
        if einsatz  > kontostand or einsatz < 0:
            print("Nicht genügend Geld vorhanden. Der Maximalbetrag ist " + str(kontostand) + ".")
        else:
            allowed_einsatz = True
    bet = {"type": "odd/even",
           "value": value,
           "einsatz": einsatz}
    return bet



def define_red_black(kontostand:int, bets : list):
    '''Wette auf Rot oder Schwarz definieren'''
    allowed_value = False
    allowed_einsatz = False
    colours = ['red', 'black', 'green']
    while allowed_value == False:
        value = str(input("Soll auf 'red', 'black' oder 'green' gesetzt werden?"))
        if value not in colours:
            print("Bitte gib entweder 'red', 'black' oder 'green' ein.")
        else:
            allowed_value = True
    while allowed_einsatz == False:
        einsatz = int(input("Wieviel möchtest du setzen? Dein Kontostand beträgt " + str(kontostand) + "."))
        if einsatz > kontostand or einsatz < 0:
            print("Nicht genügend Geld vorhanden. Der Maximalbetrag ist " + str(kontostand) + ".")
        else:
            allowed_einsatz = True
    bet = {"type": "red/black",
           "value": value,
           "einsatz": einsatz}
    return bet




def define_dozens(kontostand:int, bets : list):
    '''Wette auf Drittel definieren'''
    allowed_value = False
    allowed_einsatz = False
    while allowed_value == False:
        value = int(input("Auf welches Drittel soll gewettet werden?"))
        if value not in range(1, 4) :
            print(
                "Bitte gib entweder 1 für das erste Drittel, 2 für das zweite Drittel oder 3 für das dritte Drittel ein.")
        else:
            allowed_value = True
    while allowed_einsatz == False:
        einsatz = int(input("Wieviel möchtest du setzen? Dein Kontostand beträgt " + str(kontostand) + "."))
        if einsatz > kontostand or einsatz < 0:
            print("Nicht genügend Geld vorhanden. Der Maximalbetrag ist " + str(kontostand) + ".")
        else:
            allowed_einsatz = True
    bet = {"type": "dozens",
           "value": value,
           "einsatz": einsatz}
    return bet





def define_columns(kontostand:int, bets : list):
    '''Wette auf ganze Spalte definieren'''
    allowed_value = False
    allowed_einsatz = False
    while allowed_value == False:
        value = int(input("Auf welche Spalte soll gewettet werden?"))
        if value not in range(1, 4) :
            print("Bitte gib eine Spalte zwischen 1 und 3 ein.")
        else:
            allowed_value = True
    while allowed_einsatz == False:
        einsatz = int(input("Wieviel möchtest du setzen? Dein Kontostand beträgt " + str(kontostand) + "."))
        if einsatz > kontostand or einsatz < 0:
            print("Nicht genügend Geld vorhanden. Der Maximalbetrag ist " + str(kontostand) + ".")
        else:
            allowed_einsatz = True
    bet = {"type": "columns",
           "value": value,
           "einsatz": einsatz}
    return bet




def define_high_low(kontostand:int) ->dict:
    '''Wette auf Hälften definieren'''
    allowed_value = False
    allowed_einsatz = False
    allowed_values=["1-18", "19-36"]
    while not allowed_value:
        value = str(input("Soll auf die erste Hälfte ('1-18') oder auf die zweite Hälfte ('19-36') gewettet werden??"))
        if value not in allowed_values:
            print("Bitte gib entweder '1-18' für die erste Hälfte oder '19-36' für die zweite Hälfte ein.")
        else:
            allowed_value = True
    while not allowed_einsatz:
        einsatz = int(input("Wieviel möchtest du setzen? Dein Kontostand beträgt " + str(kontostand ) + "."))
        if einsatz > kontostand or einsatz < 0:
            print("Nicht genügend Geld vorhanden. Der Maximalbetrag ist " + str(kontostand) + ".")
        else:
            allowed_einsatz = True
    bet = {"type": "high/low",
           "value": value,
           "einsatz": einsatz}
    return bet




def spin() -> int:
    '''Generiert gefallene Zahl'''
    wert = random.randint(0, 36)
    print("Ergebnis der Drehung ist die Zahl: " + str(wert))
    return wert



def define_auswertung(wert: int, bets:list) -> int :
    gain = 0
    for bet in bets:
        if bet["type"] == "full number":
            if bet["value"] == wert:
                gain += bet["einsatz"] * 36
        if bet["type"] == "split":
            if wert in bet["value"]:
                gain += bet["einsatz"]*18
        if bet["type"] == "street":
            if wert in bet["value"]:
                gain += bet["einsatz"]*12
        if bet["type"] == "corner":
            if wert in bet["value"]:
                gain += bet["einsatz"]*9
        if bet["type"] == "six line":
            if wert in bet["value"]:
                gain += bet["einsatz"]*6
        if bet["type"] == "odd/even":
            bet_value = bet["value"]
            if numbers[wert][3] == bet_value:
                gain += bet["einsatz"]*2
        if bet["type"] == "red/black":
            bet_value = bet["value"]
            if numbers[wert][1] == bet_value:
                gain += bet["einsatz"]*2
        if bet["type"] == "dozens":
            bet_value = bet["value"]
            if numbers[wert][2] == bet_value:
                gain += bet["einsatz"]*2
        if bet["type"] == "columns":
            bet_value = bet["value"]
            if (wert % 3 +1) == bet_value or wert == 0:
                gain += bet["einsatz"]*2
        if bet["type"] == "high/low":
            bet_value = bet["value"]
            if numbers[wert][4] == bet_value:
                gain += bet["einsatz"]*2
    return gain


def main():
    weiterspielen = True
    print("Hallo zu Roulette in Leahcim-s-Casino")
    kontostand = geld_anfordern()
    while weiterspielen:
        bets, kontostand = define_bets(kontostand=kontostand)
        wert = spin()
        gain = define_auswertung(wert=wert, bets=bets)
        kontostand += gain
        print("Dein Kontostand beträgt:" + str(kontostand))
        weiterspielen = (str(input("Möchtest du weiterspielen? 'Ja' / 'Nein'")) == "Ja")
        if weiterspielen == True:
            geld = (str(input(
                "Möchtest du weiteres Geld in Chips auszahlen lassen? 'Ja' / 'Nein'")) == "Ja")
            if geld == True:
                kontostand += geld_anfordern()
            if kontostand == 0 and weiterspielen:
                print("Dein Kontostand beträgt: 0\n Zahle weiteres Geld ein!")
                kontostand += geld_anfordern()
        else:
            break



if __name__ == '__main__':
    main()




#1. Geld Anfordern --> Kontostand setzen -----> fertig
#2. Wetten setzen
#Kugel rollen lassen -----fertig
#Auswerten und Gewinn auszahlen --> Kontostand aktualisieren
#Weiterspielen?
