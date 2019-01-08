import pickle, shelve


f = open("wyniki.dat", "wb")

list1 = ["easy", "hard", "medium"]
list2 = ["level 1", "level2", "level3"]

wynik1 = pickle.load(f)
print(wynik1)
f.close()









