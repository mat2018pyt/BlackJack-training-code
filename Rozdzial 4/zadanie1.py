x = int(input("Podaj pierwszą liczbę: "))
y = int(input("Podaj drugą liczbę: "))
z = int(input("podaj co ile mam liczyc"))

"""
while x <= y:
    print(x)
    x += z
"""

for i in range(x, y+1, z):
    print(i)
