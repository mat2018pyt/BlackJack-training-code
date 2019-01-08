
"""
przysmak1 = input("Podaj nazwę pierwszego przysmaku")
przysmak2 = input("Podaj nazwę drugiego przysmaku")

print(przysmak1, przysmak2)
"""

rachunek = int(input("Suma rachunku wynosi: "))

napiwek = input("\nJaki napiwek chcesz zosawić? \nWybierz 1 dla 10% \nWybierz 2 dla 15%\nWybór: ")

if napiwek == "1":
    print("\nWysokość napiwku to", rachunek * 0.10, "zł")
elif napiwek == "2":
    print("\nWysokość napiwku to", rachunek * 0.15, "zł")
else:
    print("Błędny wybór")

input("\n\nNaciśnij ENTER aby zakończyć")


