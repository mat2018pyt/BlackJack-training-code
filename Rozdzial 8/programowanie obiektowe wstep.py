class Critter(object):

    total = 0

    def __init__(self, name):
        self.__name = name
        Critter.total += 1

    def __str__(self):
        text = "jestem " + self.__name
        return text

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("nie mozna zmienic na pusty lancuch")
        else:
            self.__name = new_name

    @staticmethod
    def status():
        print(Critter.total)

    def talk(self):
        print("Na imie mam" + self.__name)


crit1 = Critter("Adam")
crit1.talk()
crit2 = Critter("Rysiek")
crit2.talk()
print(crit1.name)
crit1.name = "Reksio"
print(crit1.name)
print(crit1)
print(Critter.total)
Critter.status()

