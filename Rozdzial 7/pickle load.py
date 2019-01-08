import pickle

f = open("wyniki.dat", "rb")
A = pickle.load(f)
B = pickle.load(f)
C = pickle.load(f)


print(A, B, C)