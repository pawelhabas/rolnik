TYPY_ZWIERZAT = dict()
TYPY_KARMY = dict()
TYPY_PRODUKTOW = dict()
ZWIERZETA = list()  # lista posiadanych zwierząt
KARMY = dict()  # lista posiadanej karmy - DICT
PORTFEL = 0  # posiadane pieniądze
SPICHLERZ = dict()  # posiadane produkty (nie karma)
CENY_SPRZEDAZY = dict()
CENY_KUPNA = dict()

TYPY_ZWIERZAT[1] = 'kura'
TYPY_KARMY[1] = 'karma dla kur'
TYPY_PRODUKTOW[1] = 'jajko'

CENY_SPRZEDAZY[1] = 1
CENY_KUPNA[1] = 3
OPERACJE_USERA = {1: 'Nakarm kurę', 2: 'Zbierz jako', 3: 'Koniec tury', 4: 'Sprzedaj na targu jajko',
                  5: 'Kup na targu karmę'}

ZWIERZETA.append(1)  # Zaczynamy z 1 kurą
ZWIERZETA.append(1)  # Zaczynamy z 1 kurą
KARMY[1] = 5  # Zaczynamy z karmą na 5 dni dla kurczaków
PORTFEL += 15  # Zaczynamy z 10 monetami


def pobierz_stan(ktory):
    global PORTFEL
    global ZWIERZETA
    global TYPY_ZWIERZAT
    global KARMY
    global TYPY_KARMY
    if ktory == 'portfel':
        return PORTFEL
    if ktory == 'zwierzeta':
        txt_zwierzeta = ''
        i = 1
        for e in ZWIERZETA:
            print(f"{i}. {TYPY_ZWIERZAT[e]}")
            txt_zwierzeta += f"{i}. {TYPY_ZWIERZAT[e]}\n"
            i += 1
        return txt_zwierzeta
    if ktory == 'karmy':
        txt_karmy = ''
        print('- Karmy:')
        i = 1
        for e in KARMY:
            print(f"{i}. {TYPY_KARMY[e]} - {KARMY[e]} porcji")
            txt_karmy += f"{i}. {TYPY_KARMY[e]} - {KARMY[e]} porcji"
            i += 1
        return txt_karmy
    return 'BRAK'

