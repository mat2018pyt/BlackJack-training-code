
slowo = input("podaj jakies slowo: ")
slowo2 = ""
i = 0
while i <= len(slowo) - 1:
    print(slowo[len(slowo)-1-i])
    slowo2 += str(slowo[(len(slowo) - 1 - i)])
    i += 1


print(slowo2)
