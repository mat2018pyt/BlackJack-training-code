import shelve


s = shelve.open("pickle.dat")

s["list3"] = [1, 2, 3]
s["list4"] = ["R", "A"]
s.sync()


print(s["list3"])



try:
    x = float(input())

except ValueError as e:
    print("wystapil blad")
    x = 65
    print(e)
else:
    print("aaaA")


print(x)



s.close()



