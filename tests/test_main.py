from src.tennis_functions import *
from prettytable import PrettyTable


def test_main():
    table = create_tennis_grand_slam_table()
    assert isinstance(table, PrettyTable)  # sicherstellen, dass Ausgabe im Dateityp Prettytable ist
    assert table.field_names == ["Jahr", "Australian Open", "French Open", "Wimbledon", "US Open"]  # Überprüfung Überschriften

    assert anzahl_slams_abfrage("Federer") == 20
    assert anzahl_slams_abfrage("Djokovic") == 20
    assert anzahl_slams_abfrage("Invalid_Player") == 0
