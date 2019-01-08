

class telewizor(object):

    def __init__(self, channel = 1, volume = 5):
        self.channel = channel
        self.volume = volume
        print("Kanał: ", channel, "Głośność: ", volume)

    def volume_change(self):
        move = input("Wciśnij + aby dać głośniej lub - aby dać ściszyć")
        if move == "+":
            self.volume += 1
        elif move == "-":
            self.volume -= 1
        else:
            print("Zły wybór")

    def change_channnel(self):
        move = int(input("Wybierz kanal od 1 do 5"))
        if 0 < move < 6:
            self.channel = move
        else:
            print("nie ma takiego kanalu")

def main():

    turnon = telewizor()
    choose = None


    while choose != "0":

        print("""

        0 - wylacz tv
        1 - zmien kanal
        2 - zmien glosnosc

        """)

        print("aktualna glosnosc to:", turnon.volume, "kanal to:", turnon.channel)
        choose = input("wybierz co chcesz zrobic")


        if choose == "1":
            turnon.change_channnel()
        elif choose == "2":
            turnon.volume_change()

    input("Koniec, nacisnij enter")

main()