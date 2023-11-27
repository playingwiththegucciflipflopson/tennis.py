from tennis_functions import *

if __name__ == "__main__":

    clear_shell()
    print_bold("GRAND SLAM SIEGER")  # Überschrift in Fett
    user_prompt = """
(1): Siegertabelle anzeigen
(2): Spieler suchen
(3): Spieler sortiert nach Anzahl Slams anzeigen
(4): Highlights von Finale nach Wunsch

"""
    choice = input(user_prompt)

    match choice:
        case "1":
            clear_shell()
            print(create_tennis_grand_slam_table())
        case "2":
            clear_shell()
            spieler_name = input("Spieler suchen: ")
            print(f"{spieler_name} hat {anzahl_slams_abfrage(spieler_name)} Slams gewonnen\n")
        case "3":
            clear_shell()
            print(anzahl_slams_tabelle())
        case "4":
            clear_shell()
            event = input("Jahr und Event eingeben: ")
            highlights(event)

    # BEISPIELE
    # print(australian_open.values())       # nur Werte (= Sieger)
    # print(australian_open.keys())         # nur Schlüssel (= Jahre)
    # print(australian_open.items())        # alles ausgeben
    # print(australian_open.get("2012"))    # Sieger 2012 wird ausgegeben
    # print(get_table())                    # Tabelle ausgeben
    # print(anzahl_slams("Nadal"))          # Anzahl Slams von Eingabe
    # print(anzahl_slams_tabelle())         # Slams pro Spieler von hoch zu niedrig
