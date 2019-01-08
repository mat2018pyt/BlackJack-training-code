import random

HANGMAN = (
"""
------
|    |
|
|
|
|
|
|
|
----------
""",
"""
------
|   |
|   O
|
|
|
|
|
|
----------
""",
"""
------
|    |
|    O
|   -+-
|
|
|
|
|
----------
""",
"""
------
|    |
|    O
|  /-+-
|
|
|
|
|
----------
""",
"""
------
|   |
|   O
| /-+-/
|
|
|
|
|
----------
""",
"""
------
|   |
|   O
| /-+-/
|   |
|
|
|
|
----------
""",
"""
------
|   |
|   O
| /-+-/
|   |
|   |
|  |
|  |
|
----------
""",
"""
------
|   |
|   O
| /-+-/
|   |
|   |
|  | |
|  | |
|
----------
""")

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("PIES", "WROCŁAW", "KUCHNIA", "ZABAWA")
word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []

while so_far != word and MAX_WRONG > wrong:
    print(HANGMAN[wrong])
    print("\nWykorzystałeś już następujące litery:", used)
    print("\nZagadkowe słowo wygląda w tej chwili tak:", so_far)

    guess = input("Podaj literę: ")
    guess = guess.upper()

    while guess in used:
        print("Wybrana litera została już wybrana, podaj inną: ")
        guess = (input("Podaj literę: "))
        guess.upper()

    used.append(guess)

    if guess in word:
        print("\nTak, wybrana litera znajduje się  zagadkowym słowie!")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print("\nWubrana litera nie znajduje się w zagadkowym słowie")
        wrong += 1


if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nZostałeś powieszony!")
else:
    print("\nBrawo ! Odgadadłeś!")

print("\nZagadkowe słowo to:", word)
input("\nAby zakończyć naciśnij ENTER")
