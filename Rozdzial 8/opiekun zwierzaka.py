import sys, random

class Critter(object):

    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        text = self.name + str(self.hunger) + str(self.boredom)
        return text

    def __pass_time(self):
            self.boredom += 1
            self.hunger += 1

    @property
    def mood(self):
        unhapiness = self.boredom + self.hunger
        if unhapiness < 3:
            m = "szczesliwy"
        elif 3 <= unhapiness < 5:
            m = "zadowolony"
        elif 5 <= unhapiness < 8:
            m = "zdenerwowany"
        elif 8 <= unhapiness:
            m = "wsciekly"
        return m

    def talk(self):
        print("zwierzak", self.name, "mowi ze jest", self.mood)
        self.__pass_time()

    def eat(self, food = 2):
        food = int(input("jak dużo chcesz dac jedzenia?: "))
        if self.hunger >= 2:
            print(self.name, "zostal nakarmiony")
            self.hunger -= food
        else:
            print(self.name, "jest nakarmiony i nie chce jesc")


    def play(self, fun = 2):

        if self.boredom >= 2:
            self.boredom -= fun
            print(self.name, "pobawil sie")
        else:
            print(self.name, "nie chce sie bawic")


def main():
    crit = []
    for i in range(3):
        crit_name = input("Podaj imie dla zwierzaczka nr")
        crit.append(Critter(crit_name, random.randint(1, 4), random.randint(1, 4)))


    choice = None

    while choice != 0:
        print("""
            0 - Zakończ program.
            1 - Słuchaj swojego zwierzaka.
            2 - Nakarm swojego zwierzaka.
            3 - Pobaw się ze swoim zwierzakiem.
        """)

        choice = input("Wybierasz: ")

        if choice == "0":
            input("\n\nAby zakończyć naciśnij ENTER.")

        elif choice == "1":
            for i in range(len(crit)):
                crit[i].talk()

        elif choice == "2":
            for i in range(len(crit)):
                crit[i].eat()

        elif choice == "3":
            fun = int(input("ile czasu chcesz poswiecic na zabawe?: "))
            for i in range(len(crit)):
                crit[i].play(fun)

        elif choice == "4":
            for i in range(len(crit)):
                print(crit[i])

        else:
            print("Zły wybór, wybierz jeszcze raz: ")
            choice = input()

main()

