choice = ""
atributs = {"Siła":0, "Zdrowie":0, "Mądrość":0, "Zręczność":0}
points = 30

while choice != 0:

    print("""
    \t\t\t*** MENU ***

    0 - Wyjdź z programu
    1 - Pokaż aktualne wartości atrybutów
    2 - Rozdysponuj punkty
    3 - Zmodyfikuj wartości atrybutów

    \t\t\t************

    """
    )

    choice = (input("Twój wybór to: "))


    if choice == "0":
        input("Koniec programu, aby zakończyć naciśnij ENTER")
        break

    elif choice == "1":
        print(atributs)
        input("\nAby przejść do MENU naciśnij ENTER")

    elif choice == "2":
        if points > 0:
            print("\nMasz:", str(points), "do rozdysponowania")
            atribute = input("Podaj atrybut który chcesz doładować: ")
            while atribute not in atributs:
                print("Nie ma takiego atrubuty, podaj atrybut jeszcze raz")
                atribute = input("Podaj atrybut który chcesz doładować: ")


            value = input("Ile punktów chcesz przeznaczyć dla tego atrubutu?")
            while int(value) > points:
                value = input("Nie masz tylu punktów, podaj wartość jeszcze raz: ")

            atributs[atribute] += int(value)
            points -= int(value)

        else:
            print("Nie masz punktów do rozdysponowania, musisz odzyskać punkty modyfikując inne atrybuty.")

    elif choice == "3":
        atribute = input("Podaj atrybut który chcesz zmodyfikować: ")
        while atribute not in atributs:
            print("Nie ma takiego atrubuty, podaj atrybut jeszcze raz")
            atribute = input("Podaj atrybut który chcesz doładować: ")

        print("Chcesz dodać czy odjąć wartość od atrybutu?"
              "Wybierz U - aby odjąć, D - aby dodać")
        choice = input()
        while choice != "D" and choice != "U":
            choice = input("Podaj jeszcze raz:")

        value = (input("Podaj wartość o jaką chcesz zmodyfikować atrybut"))
        if choice == "U":
            while int(value) > atributs[atribute]:
                value = input("Chcesz odjąć więcej punktów niż atrybut ma wartości, podaj wartość do odjęcia jeszcze raz: ")
            atributs[atribute] -= int(value)
            points += int(value)
        elif choice == "D":
            while int(value) > points:
                value = input("Nie masz tylu punktów, podaj wartość jeszcze raz: ")
            atributs[atribute] += int(value)
            points -= int(value)











