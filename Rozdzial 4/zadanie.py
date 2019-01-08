"""
slowo = input("Wprowadz jakies slowo: ")

for i in slowo:
    print(i)


input("\n\nAby zakończyć naciśnij ENTER")


komunikat = input("Wprowadz kominikat: ")
licznik = 0
for i in komunikat:
    if "a" == i:
        licznik += 1
    else:
        continue

print(licznik)


"""
import random


SLOWA = ("konstelnacja", "usatysfakcjonowany", "determinować", "domek", "Rico", "Bonka")
slowo = random.choice(SLOWA)
odpowiedz = slowo
slowo_mix = ""

while slowo:
    i = random.randint(0, len(slowo)-1)
    slowo_mix += slowo[i]
    slowo = slowo[:i] + slowo[(i+1):]


print("\t\t\tWitaj w programie wymieszane litery!!!")
print("\n\n\t\t\tZgadnij jakie to słowo:", slowo_mix)
proba = input()
i = 1
j = 1
while proba != odpowiedz:
    print("Spróbuj jeszcze raz")
    print("To jest Twoja", i+1,"próba")    
    if i % 3 == 0:
        print("Podpowiedź:", odpowiedz[:j]+("_ " * (len(odpowiedz) - j)),
              "I otrzymujesz -", j,"punktów", "Masz teraz:", len(odpowiedz) - j + 1,
              "punktów")
        j += 1
    proba = input()
    i += 1
    
    
    
print("Zdobyłaś:", len(odpowiedz) - j + 1,"punktów")
print("Brawo !!! " * 5, end=" ")
input("\n\nAby zakończyć naciśnij ENTER")
    
        









"""
wyraz = "gajowicka"
litery = "aąeęioóuy"
new_message = ""

for letter in wyraz:
    if letter.lower() not in litery:
        new_message += letter
        print(new_message)
"""
