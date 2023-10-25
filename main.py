from data_slams import australian_open, french_open, wimbledon, us_open
from os import system
from prettytable import PrettyTable
from collections import Counter
import webbrowser


def clear():  # shell clearen
    system('clear')


def get_table() -> PrettyTable:
    table = PrettyTable(["Jahr", "Australian Open", "French Open", "Wimbledon", "US Open"])
    lst = []
    for b in australian_open.keys():
        lst.append(b)
    u = 0
    for a in australian_open:
        table.add_row([lst[u], australian_open[a], french_open[a], wimbledon[a], us_open[a]])
        u = u+1

    return table


def anzahl_slams_abfrage(a: str) -> int:  # geht soweit
    ao = list(australian_open.values())
    fo = list(french_open.values())
    wm = list(wimbledon.values())
    us = list(us_open.values())

    anzahl = ao.count(a) + fo.count(a) + wm.count(a) + us.count(a)
    if a not in ao and a not in fo and a not in wm and a not in us:
        raise NameError
    else:
        return (anzahl)


def anzahl_slams_tabelle() -> PrettyTable:
    table = PrettyTable(["Spieler", "Slams"])

    xs = []  # leere Liste
    for x in australian_open.values():  # Zählen wie oft jeder Australian Open gewonnnen hat
        xs.append(x)
    for x in french_open.values():  # Zählen wie oft jeder French Open gewonnnen hat
        xs.append(x)
    for x in wimbledon.values():  # Zählen wie oft jeder Wimbledon gewonnnen hat
        xs.append(x)
    for x in us_open.values():  # Zählen wie oft jeder US-Open gewonnnen hat
        xs.append(x)

    while ("" in xs):  # leere Strings aus Liste raus
        xs.remove("")
    while ("-" in xs):  # - aus Liste raus
        xs.remove("-")

    counted = dict(Counter(xs))  # counter initiieren
    counted_sorted = dict(sorted(counted.items(), key=lambda item: item[1], reverse=True))  # sortieren (umgekehrt)

    c = []
    for b in counted_sorted.keys():  # Namen in Liste
        c.append(b)

    u = 0  # lauft durch
    for a in counted_sorted:  # Rückgabe Tabelle, a ist keine Zahl!!!!
        table.add_row([c[u], counted_sorted[a]])
        u = u+1

    return table


def highlights(a: str) -> None: #fehlen noch viele
    liste = a.split()
    url = None

    if liste[:2] == ["Australian", "Open"]:
        if liste[2] == "2022":
            url = "https://www.youtube.com/watch?v=v27M_RgrLzU"
        if liste[2] == "2023":
            url = "https://www.youtube.com/watch?v=N2Dtsx-6aDc"

    if liste[:2] == ["French", "Open"]:
        if liste[2] == "2022":
            url = "https://www.youtube.com/watch?v=RO52Y8SOIUU"
        if liste[2] == "2023":
            url = "https://www.youtube.com/watch?v=fLoKlPLJOjY"

    if liste[:1] == "Wimbledon":
        if liste[1] == "2022":
            url = "https://www.youtube.com/watch?v=ZwI5aYBofo8"
        if liste[2] == "2023":
            url = "https://www.youtube.com/watch?v=K-VmllVIOXA"

    if liste[:2] == ["US", "Open"]:
        if liste[2] == "2022":
            url = "https://www.youtube.com/watch?v=SEFnfcfvLkw"
        if liste[2] == "2023":
            url = "https://www.youtube.com/watch?v=3pNQ6hDwBPg"

    if url is not None:
        webbrowser.open(url,new=1)
    else:
        raise NameError

if __name__ == "__main__":
    clear()
    # print(australian_open.values())       # nur Werte (= Sieger)
    # print(australian_open.keys())         # nur Schlüssel (= Jahre)
    # print(australian_open.items())        # alles ausgeben
    # print(australian_open.get("2012"))    # Sieger 2012 wird ausgegeben
    # print(get_table())                    # Tabelle ausgeben
    # print(anzahl_slams("Nadal"))          # Anzahl Slams von Eingabe
    # print(anzahl_slams_tabelle())         # Slams pro Spieler von hoch zu niedrig

##############################################################################################
    print("\033[1m" + "GRAND SLAM SIEGER\n" + "\033[0m") # bold commands

    choice = input("(1): Siegertabelle anzeigen\n(2): Spieler suchen\n(3): Spieler sortiert nach Anzahl Slams anzeigen\n(4): Highlights von Finale nach Wunsch\n\n")
    
    match choice:
        case "1":
            clear()
            print(get_table())
        case "2":
            clear()
            user = input("Spieler suchen: ")
            print(f"{user} hat", anzahl_slams_abfrage(user), "Slams gewonnen\n")
        case "3":
            clear()
            print(anzahl_slams_tabelle())
        case "4":
            clear()
            user = input("Jahr und Event eingeben: ")
            highlights(user)
