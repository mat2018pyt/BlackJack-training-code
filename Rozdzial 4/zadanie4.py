import random


SLOWA = ("Bonka", "Rico", "Domek")
slowo = random.choice(SLOWA)

print("\nW wylosowanymm słowie znajduje się:", len(slowo), "liter\n\n")

print("Możesz zadać mi 5 pytań, czy wybrana litera znajduje się w szukanym haśle")   
for i in range(1, 6):
    print("\nPytanie nr:", i)
    litera = input()
    if litera in slowo:
        print("\ntak")
    else:
        print("\nnie")
    odpowiedz = input("\nJeśli wiesz to wpisz poprawną odpowiedź, lub naciśnij ENTER aby zapytać o kolejną literę")
    if odpowiedz == slowo:
        print("Brawo!!! Zgadłaś")
    else:
        continue
while odpowiedz != slowo:
    odpowiedz = input("\nTwoja odpowiedź to: ")
    if odpowiedz == slowo:
            print("Brawo!!! Zgadłaś")
    else:
        print("Żle, jeszcze raz")
  



