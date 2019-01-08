# Turniej wiedzy
# Gra sprawdzająca wiedzę ogólną, odczytująca dane ze zwykłego pliku tekstowego

import sys, pickle

def open_file(file_name, mode):
    """Otwórz plik."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Nie można otworzyć pliku", file_name, "Program zostanie zakończony.\n", e)
        input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Zwróć kolejny wiersz pliku kwiz po sformatowaniu go."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Zwróć kolejny blok danych z pliku kwiz."""
    category = next_line(the_file)

    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    points = next_line(the_file)

    return category, question, answers, correct, explanation, points

def welcome(title):
    """Przywitaj gracza i pobierz jego nazwę."""
    print("\t\t Witaj w turnieju wiedzy!\n")
    print("\t\t", title, "\n")

def main():
    trivia_file = open_file("kwiz.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    name = input("Podaj swoje imie: ")
    score = 0

    # pobierz pierwszy blok
    category, question, answers, correct, explanation, points = next_block(trivia_file)

    while category:

        # zadaj pytanie
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # uzyskaj odpowiedź
        answer = input("Jaka jest Twoja odpowiedź?: ")

        # sprawdź odpowiedź
        if answer == correct:
            print("\nOdpowiedź prawidłowa!", end=" ")
            score += int(points)
        else:
            print("\nOdpowiedź niepoprawna.", end=" ")
        print(explanation)
        print("Wynik:", score, "\n\n")

        # pobierz kolejny blok
        category, question, answers, correct, explanation, points = next_block(trivia_file)

    trivia_file.close()
    print("To było ostatnie pytanie!")
    print("Twój końcowy wynik wynosi", score)
    return name, score





game = input("Jeśli chcesz grać naciśnij 1, jeśli zakończyć naciśnij ENTER")
list = []
while game == "1":
    name, score = main()
    entry = [score, name]
    list.append(entry)
    list.sort(reverse=True)
    list = list[:3]
    f = open("wyniki.txt", "w")
    for entry in list:
        score, name = entry
        print("\n", name, score)
        f.writelines(str(entry))
    f.close()

    game = input("Jeśli chcesz grać naciśnij 1, jeśli zakończyć naciśnij ENTER")

