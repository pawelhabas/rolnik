# rolnik
small game for kids but not only for them

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
