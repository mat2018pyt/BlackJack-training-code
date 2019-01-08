def birthday(name, age):
    print(name, "masz już", age, "lat!")

def birthday2(name = "Iwona", age = 54):
    print(name, "masz już", age, "lat!")


print(birthday("Janusz", 18))
print(birthday2(age = "Anna", name = 90))
