from data_slams import australian_open, french_open, wimbledon, us_open
from os import system
from prettytable import PrettyTable
from collections import Counter
import webbrowser
import platform


def clear():  # shell clearen
    betriebssystem = platform.system()  # Abfrage welches Betriebssystem Nutzer verwendet

    match betriebssystem:
        case "Windows":  # Windows
            system("cls")
        case _:  # alle anderen OS
            system("clear")


def create_tennis_grand_slam_table() -> PrettyTable:
    table = PrettyTable(["Jahr", "Australian Open", "French Open", "Wimbledon", "US Open"])  # Tabelle mit Überschriften erstellt
    lst = []
    for year in australian_open.keys():  # Die Jahre werden gesammelt
        lst.append(year)
    year_index = 0
    for year in australian_open:  # Inhalt Tabelle wird errechnet
        table.add_row([lst[year_index], australian_open[year], french_open[year], wimbledon[year], us_open[year]])
        year_index += 1

    return table


def anzahl_slams_abfrage(spieler_name: str) -> int:
    ao = list(australian_open.values())
    fo = list(french_open.values())
    wm = list(wimbledon.values())
    us = list(us_open.values())

    anzahl = ao.count(spieler_name) + fo.count(spieler_name) + wm.count(spieler_name) + us.count(spieler_name)  # Anzahl an gewonnenen Slams wird gezählt

    if spieler_name not in ao and spieler_name not in fo and spieler_name not in wm and spieler_name not in us:  # Falls Spieler keine Slams hat
        raise NameError("Spieler nicht gefunden")
    else:
        return anzahl


def anzahl_slams_tabelle() -> PrettyTable:
    table = PrettyTable(["Spieler", "Slams"])  # Tabelle mit Überschriften erstellt

    wins = []  # leere Liste
    for x in australian_open.values():  # Zählen wie oft jeder Australian Open gewonnnen hat
        wins.append(x)
    for x in french_open.values():  # Zählen wie oft jeder French Open gewonnnen hat
        wins.append(x)
    for x in wimbledon.values():  # Zählen wie oft jeder Wimbledon gewonnnen hat
        wins.append(x)
    for x in us_open.values():  # Zählen wie oft jeder US-Open gewonnnen hat
        wins.append(x)

    while ("" in wins):  # leere Strings aus Liste raus
        wins.remove("")
    while ("-" in wins):  # - aus Liste raus
        wins.remove("-")

    counted = dict(Counter(wins))  # counter initiieren
    counted_sorted = dict(sorted(counted.items(), key=lambda item: item[1], reverse=True))  # sortieren (umgekehrt)

    namen = []
    for b in counted_sorted.keys():  # Namen in Liste
        namen.append(b)

    walker = 0  # lauft durch
    for a in counted_sorted:  # Rückgabe Tabelle, a ist keine Zahl!!!!
        table.add_row([namen[walker], counted_sorted[a]])
        walker += 1

    return table


def highlights(event_year: str) -> None:  # fehlen noch viele
    url = None

    match event_year.split():
        case ["Australian", "Open", "2022"]:
            url = "https://www.youtube.com/watch?v=v27M_RgrLzU"
        case ["Australian", "Open", "2023"]:
            url = "https://www.youtube.com/watch?v=N2Dtsx-6aDc"
        case ["French", "Open", "2022"]:
            url = "https://www.youtube.com/watch?v=RO52Y8SOIUU"
        case ["French", "Open", "2023"]:
            url = "https://www.youtube.com/watch?v=fLoKlPLJOjY"
        case ["Wimbledon", year]:
            if year == "2022":
                url = "https://www.youtube.com/watch?v=ZwI5aYBofo8"
            elif year == "2023":
                url = "https://www.youtube.com/watch?v=K-VmllVIOXA"
        case ["US", "Open", "2022"]:
            url = "https://www.youtube.com/watch?v=SEFnfcfvLkw"
        case ["US", "Open", "2023"]:
            url = "https://www.youtube.com/watch?v=3pNQ6hDwBPg"
        case _:
            print("Die Eingabe konnte nicht erkannt werden.")

    if url is not None:
        webbrowser.open(url, new=1)


def display_menu():  # Anzeige Bildschirm
    clear()

    def print_bold(text):
        bold_text = "\033[1m" + text + "\033[0m"
        print(bold_text)
    print_bold("GRAND SLAM SIEGER")  # Überschrift in Fett

    user_prompt = """
(1): Siegertabelle anzeigen
(2): Spieler suchen
(3): Spieler sortiert nach Anzahl Slams anzeigen
(4): Highlights von Finale nach Wunsch

"""
    choice = input(user_prompt)
    return choice


if __name__ == "__main__":

    choice = display_menu()

    match choice:
        case "1":
            clear()
            print(create_tennis_grand_slam_table())
        case "2":
            clear()
            user = input("Spieler suchen: ")
            print(f"{user} hat {anzahl_slams_abfrage(user)} Slams gewonnen\n")
        case "3":
            clear()
            print(anzahl_slams_tabelle())
        case "4":
            clear()
            user = input("Jahr und Event eingeben: ")
            highlights(user)

    # BEISPIELE
    # print(australian_open.values())       # nur Werte (= Sieger)
    # print(australian_open.keys())         # nur Schlüssel (= Jahre)
    # print(australian_open.items())        # alles ausgeben
    # print(australian_open.get("2012"))    # Sieger 2012 wird ausgegeben
    # print(get_table())                    # Tabelle ausgeben
    # print(anzahl_slams("Nadal"))          # Anzahl Slams von Eingabe
    # print(anzahl_slams_tabelle())         # Slams pro Spieler von hoch zu niedrig
