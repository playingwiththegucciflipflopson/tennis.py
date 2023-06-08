from os import system
from prettytable import PrettyTable


def clear():  # shell clearen
    system('clear')


australian_open = {"2005": "Safin", "2006": "Federer", "2007": "Federer",
                   "2008": "Djokovic", "2009": "Nadal", "2010": "Federer",
                   "2011": "Djokovic", "2012": "Djokovic", "2013": "Djokovic",
                   "2014": "Wawrinka", "2015": "Djokovic", "2016": "Djokovic",
                   "2017": "Federer", "2018": "Federer", "2019": "Djokovic",
                   "2020": "Djokovic", "2021": "Djokovic", "2022": "Nadal",
                   "2023": "Djokovic"}

french_open = {"2005": "Nadal", "2006": "Nadal", "2007": "Nadal",
                   "2008": "Nadal", "2009": "Federer", "2010": "Nadal",
                   "2011": "Nadal", "2012": "Nadal", "2013": "Nadal",
                   "2014": "Nadal", "2015": "Wawrinka", "2016": "Djokovic",
                   "2017": "Nadal", "2018": "Nadal", "2019": "Nadal",
                   "2020": "Nadal", "2021": "Djokovic", "2022": "Nadal", 
                   "2023": ""}

wimbledon = {"2005": "Federer", "2006": "Federer", "2007": "Federer",
                   "2008": "Nadal", "2009": "Federer", "2010": "Nadal",
                   "2011": "Djokovic", "2012": "Federer", "2013": "Murray",
                   "2014": "Djokovic", "2015": "Djokovic", "2016": "Murray",
                   "2017": "Federer", "2018": "Djokovic", "2019": "Djokovic",
                   "2020": "", "2021": "Djokovic", "2022": "Djokovic", 
                   "2023": ""}

us_open = {"2005": "Federer", "2006": "Federer", "2007": "Federer",
                   "2008": "Federer", "2009": "Del Potro", "2010": "Nadal",
                   "2011": "Djokovic", "2012": "Murray", "2013": "Nadal",
                   "2014": "Cilic", "2015": "Djokovic", "2016": "Wawrinka",
                   "2017": "Nadal", "2018": "Djokovic", "2019": "Nadal",
                   "2020": "Thiem", "2021": "Medvedev", "2022": "Alcaraz", 
                   "2023": ""}


def get_table():
    table = PrettyTable(["Jahr", "Australian Open", "French Open", "Wimbledon", "US Open"])
    c = []
    for b in australian_open.keys():
        c.append(b)
    for a in australian_open:
        table.add_row([c[int(a)-2005], australian_open[a], french_open[a], wimbledon[a], us_open[a]])

    return table


if __name__ == "__main__":
    clear()
    # print(australian_open.values())       #nur Werte (=Sieger)
    # print(australian_open.keys())         #nur Schlüssel (=Jahre)
    # print(australian_open.items())        #alles ausgeben
    # print(australian_open.get("2012"))    #Sieger 2012 wird ausgegeben
    print(get_table())