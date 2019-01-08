"""
import random

a = random.randint(1, 6)
b = random.randint(1, 6)

print("Liczby jakie wyrzuciłeś to:", a, "i", b, "ich suma to", int(a) + int(b))


input("\nAby zakończyć naciśnij ENTER")



import random

rzut = random.randint(1,2)
i = 1
orzel = 0
reszka = 0

while i <= 100:
    if rzut == 1:
        orzel += 1
    elif rzut == 2:
        reszka += 1
    i += 1
    rzut = random.randint(1,2)

print("Liczba orłów to:", orzel, ", natomiast liczba reszek to:", reszka)
"""

import random


def ask_number(question, low, high):

    liczba = int()
    while liczba > high or liczba < low:
        liczba = int(input(question))
    return liczba

liczba = ask_number("Podaj liczbe: ", 100, 1)

strzal = int()
licznik = 0
while strzal != liczba:
    strzal = random.randint(1,100)
    licznik += 1
    print("\nKomputer strzelił:", strzal, "jest to próba nr:", licznik)


input("\n\nAby zakończyć naciśnij ENTER")





