scores = []
choice = None

while choice != "0":
    print(
        """
        Najlepsze wyniki
        0 - zakończ
        1 - pokaż wyniki
        2 - dodaj wynik
        3 - usuń wynik
        4 - posortuj wyniki
        """
    )

    choice = input("Twoj wybor to: ")

    if choice == "1":
        for entry in scores:
            score, name = entry
            print("\n", name, score)

    elif choice == "2":
        name = input("Dla którego gracza chcesz wprowadzić wynik?: ")
        score = int(input("\nJaki wynik chcesz dodać? "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]

    elif choice == "3":
        score = int(input("\nKtóry wynik chcesz usunąć? "))
        if score in scores:
            scores.remove(score)
        else:
            print(score, "nie ma takiego wyniku")

    elif choice == "4":
        scores.sort()

    elif choice == "0":
        print("Koniec")
        input("\nNaciśnij ENTER aby zakończyć")
        break

    else:
        print("Niestety błędny wybór!")
