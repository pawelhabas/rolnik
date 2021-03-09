"""
To jest gra Rolnik

zaczynamy z kurą i odrobiną karmy dla kurczaków.

w każdej turze możemy nakarmić zwierzę a po karmieniu otrzymać produkt spożywczy
UWAGA jak nie nakarmimy zwierzęcia to ono nie umiera ale też nic nie zyskujemy.

Produkty spożywcze możemy sprzedawać na targu.
Na targu możemy sprzedawać też zwierzęta.
Na targu kupujemy też karmę dla zwierząt.
Jak zawsze zwierzęta drożej kupujemy a taniej sprzedajemy.

za zarobione pieniądze możemy kupować kolejne zwierzęta i karmę dla nich.

możemy również kupować pomocne narzędzia/budynki.
np.:
- do karmienia możemy kupić wiadro i karmić 2 zwierzęta za 1 kliknięciem
- do karmienia możemy kubić taczkę i karmić 5 zwierząt na raz
- do zbierania jajek od kur możemy kubić koszyk i zbierać po 5 jajek na raz

każdy gracz ma swój profil zapisywany w plikach tekstowych (na początek txt, ale chciałbym json)

Po uruchomieniu gry podajemy swoje imię by załadować odpowiedni profil.

Gra okienkowa, mamy pasek stanu, a poniżej możliwe 2 okna: gospodarstwo i targ
Na gospodarstwie widzimy posiadane zwierzęta w formie tekstowej (docelowo graficznej) wraz z ich ilością
    oraz posiadane budynki oraz narzędzia

----------------
AD.1 Możemy sprzedawać hurtowo np. 10 jaj zamiast kosztować 10 monet przy zwykłej sprzedarzy
    hurtowo sprzedamy za 11 monet (+10%)

AD.2 Każde zwierzę jest obiektem klasy ZWIERZE()
    każde zwierze posiada kilka parametrów:
    - karmienie
    - dojenie

AD.3 Cennik sprzedaży i kupna powinny być DICT (DICT):
    - ID pozycji
    - Wartości:
        - nazwa
        - cena
        - grupa produktów   # czyli którego zwierzęcia dotyczy


"""
from PyQt5.QtWidgets import QApplication

TYPY_ZWIERZAT = dict()
TYPY_KARMY = dict()
TYPY_PRODUKTOW = dict()
ZWIERZETA = list()  # lista posiadanych zwierząt
KARMY = dict()  # lista posiadanej karmy - DICT
# PORTFEL = 0  # posiadane pieniądze
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
KARMY[1] = 5  # Zaczynamy z karmą na 5 dni dla kurczaków
# PORTFEL += 10  # Zaczynamy z 10 monetami

print(f'Witaj na gospodarce.')

# print(f'Aktualnie posiadasz {PORTFEL} monet oraz:\n- Zwierzęta:')
# txt_zwierzeta = ''
# i = 1
# for e in ZWIERZETA:
#     print(f"{i}. {TYPY_ZWIERZAT[e]}")
#     txt_zwierzeta += f"{i}. {TYPY_ZWIERZAT[e]}"
#     i += 1
# txt_karmy = ''
# print('- Karmy:')
# i = 1
# for e in KARMY:
#     print(f"{i}. {TYPY_KARMY[e]} - {KARMY[e]} porcji")
#     txt_karmy += f"{i}. {TYPY_KARMY[e]} - {KARMY[e]} porcji"
#     i += 1
# dalej = True
# while True:
#     for e in OPERACJE_USERA:
#         print(f"{e} - {OPERACJE_USERA[e]}")
#
#     opcja = input('Co chcesz zrobić? ')
#     if opcja == '3':
#         print('Koniec tury')
#         break


if __name__ == '__main__':
    import sys
    import okno

    app = QApplication(sys.argv)
    my_window = okno.MyWindow()
    # my_window.ustaw_stat_war('portfel', PORTFEL)
    my_window.pobierz_stan()
    # my_window.ustaw_stat_war('zwierzeta', txt_zwierzeta)
    # my_window.ustaw_stat_war('karma', txt_karmy)
    # my_window.ustaw_stat_war('spichlerz', 'PUSTO')
    # print(my_window.stat_labels_war['portfel'])

    my_window.pokaz()
    sys.exit(app.exec_())
