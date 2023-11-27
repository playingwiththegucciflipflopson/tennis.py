from data_slams import *
from os import system
from prettytable import PrettyTable
from collections import Counter
import webbrowser
import platform


def print_bold(text):
    '''
    Funktion, welche Text fett druckt.
    '''
    bold_text = "\033[1m" + text + "\033[0m"
    print(bold_text)


def clear_shell():
    '''
    Funktion, welche Shell cleared.
    '''
    betriebssystem = platform.system()  # Abfrage welches Betriebssystem Nutzer verwendet

    match betriebssystem:
        case "Windows":  # Windows
            system("cls")
        case _:  # alle anderen OS
            system("clear")


def create_tennis_grand_slam_table() -> PrettyTable:
    '''
    Funktion, welche PrettyTable zu den Siegern der Grand-Slam Turniere zurückgibt.
    '''
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
    '''
    Funktion, welche den Nutzer einen Spieler suchen lässt und die Anzahl an gewonnenen Grand-Slam Titeln zurückgibt.
    '''
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
    '''
    Funktion, welche ein PrettyTable mit den Grand-Slam Sieger sortiert nach Anzahl der Titel zurückgibt.
    '''
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
    '''
    Funktion, welche den Nutzer Highlights von einem Finale suchen lässt und entsprechendes Video im Webbrowser startet.
    '''
    url = None

    match event_year.split():
        case ["Australian", "Open", "2000"]:
            url = "https://www.youtube.com/watch?v=p_0HDlVkwKY"
        case ["Australian", "Open", "2001"]:
            url = "https://www.youtube.com/watch?v=mRCSXcg36kY"
        case ["Australian", "Open", "2002"]:
            url = "https://www.youtube.com/watch?v=536yyv9rWno"
        case ["Australian", "Open", "2003"]:
            url = "https://www.youtube.com/watch?v=CO7AVEmKUXw"
        case ["Australian", "Open", "2004"]:
            url = "https://www.youtube.com/watch?v=6HLprbnRKfI"
        case ["Australian", "Open", "2005"]:
            url = "https://www.youtube.com/watch?v=44cnvEJ8mjs"
        case ["Australian", "Open", "2006"]:
            url = "https://www.youtube.com/watch?v=HD1nLtt8s68"
        case ["Australian", "Open", "2007"]:
            url = "https://www.youtube.com/watch?v=XN9WtTCLOxg"
        case ["Australian", "Open", "2008"]:
            url = "https://www.youtube.com/watch?v=N9RJ0I9Ivhs"
        case ["Australian", "Open", "2009"]:
            url = "https://www.youtube.com/watch?v=zZO7saJQRxw"
        case ["Australian", "Open", "2010"]:
            url = "https://www.youtube.com/watch?v=TBixkheoQQU"
        case ["Australian", "Open", "2011"]:
            url = "https://www.youtube.com/watch?v=T9_-41naFGw"
        case ["Australian", "Open", "2012"]:
            url = "https://www.youtube.com/watch?v=-kaaXz4IgrA"
        case ["Australian", "Open", "2013"]:
            url = "https://www.youtube.com/watch?v=dOuCulN1aqg"
        case ["Australian", "Open", "2014"]:
            url = "https://www.youtube.com/watch?v=9aACpPSdIpI"
        case ["Australian", "Open", "2015"]:
            url = "https://www.youtube.com/watch?v=RXmp-ezEEQE"
        case ["Australian", "Open", "2016"]:
            url = "https://www.youtube.com/watch?v=oz-rLCx-iU8"
        case ["Australian", "Open", "2017"]:
            url = "https://www.youtube.com/watch?v=STAFMBSRDJk"
        case ["Australian", "Open", "2018"]:
            url = "https://www.youtube.com/watch?v=8DSHQvlMlVA"
        case ["Australian", "Open", "2019"]:
            url = "https://www.youtube.com/watch?v=4EVOO_wuUkM"
        case ["Australian", "Open", "2020"]:
            url = "https://www.youtube.com/watch?v=0FsIdkTFLms"
        case ["Australian", "Open", "2021"]:
            url = "https://www.youtube.com/watch?v=w4N_28vdS-Q"
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
