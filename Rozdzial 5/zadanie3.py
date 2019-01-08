pair = {}
choice = ""

while choice != "0":

    print("""
    \t\t\t***MENU***
    0 - Zakończ
    1 - Dodaj
    2 - Zmień
    3 - Usuń
    """
          )

    choice = input("Wybierz pozycję w MENU: ")

    if choice == "1":
        term = input("\nPodaj imię i nazwisko: ")
        while term in pair:
            print("Takie imię i nazwisko już istnieje, proszę podać inne.")
            term = input()
        pair[term] =
pair[term] = term.lower()

print(pair[term])

