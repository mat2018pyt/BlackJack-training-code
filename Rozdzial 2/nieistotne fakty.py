


imie = input("Cześć!, Jak masz na imię? ")
wiek = int(input("Ile lat masz {}? ".format(imie)))
waga = int(input("Ile ważysz? "))

print("Jeśli poeta ee cummings wysłał by do Ciebie wiadomość e-mail, \
zwrócił by się do Ciebie ",
      imie.lower())
print("Ale jeśli byłby wściekły, nazwałby Cię " + imie.upper())
print()
print("Małe dziecko wołało by Cię: " + imie + imie + imie + imie)
print()
print("Żyjesz już ponad ", wiek * 365 * 24 * 60 * 60, " sekund")
print()
print("Czy wiesz, że Twoja waga na Księżycu to ", waga / 6, " kg")
print("\nNatomiast na Słońcu ",imie," ważyła by aż: ", waga * 27.1, " kg !!!")
print("\a")



input("\n\nAby zakończyć program, naciśnij klawisz ENTER")
