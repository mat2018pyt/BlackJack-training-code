choice = None
dictionary = {"1":"A", "2":"B", "3":"C"}

while choice != "0":

    print("""
    Translator slangu komputerowego
    0 - zakończ
    1 - znajdź termin
    2 - dodaj nowy termin
    3 - zmień definicję terminu
    4 - usuń termin
    """
    )

    choice = input("\nWybierasz: ")

    if choice == "0":
        print("\nKoniec programu")
        input("\nAby zakończyć naciśnij ENTER")
        break

    elif choice == "1":
        term = input("Podaj szukaną wartości w słowniku: ")
        if term in dictionary:
            print("\n", term, ":", dictionary[term])
        else:
            print("Nie ma takiej wartości")
        
    elif choice == "2":
        term = input("\nJaki termin chcesz dodać?: ")
        if term in dictionary:
            print("Pozycja już istnieje, wybierz inną.")
        else:
            definition = input("Podaj definicję dla terminu: ")
            dictionary[term] = definition
            print("Termin został dodany. \n")

    elif choice == "3":
        term = input("\nPodaj termin, który chcesz zmienić: ")
        if term in dictionary:
            definition = input("Podaj nową definicję: ")
            dictionary[term] = definition
        else:
            print("Brak takiego terminu.")

    elif choice == "4":
        term = input("\nPodaj termin do usunięcia: ")
        if term in dictionary:
            del dictionary[term]
            print("Termin został usunięty.")
        else:
            print("Brak takiego terminu.")
