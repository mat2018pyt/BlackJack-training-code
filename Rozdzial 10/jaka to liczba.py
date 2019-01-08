from tkinter import *
import random


class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.tries = 0
        self.number = None

    def create_widgets(self):

        Label(self,
              text = "Kliknij aby wylosowac liczbe od 1 do 10:"
              ).grid(row = 0, column = 0)
        self.bttn1 = Button(self, text = "LOSUJ", command = self.draw_number)
        self.bttn1.grid(row = 0, column = 1)

        Label(self,
              text = "Odgadnij ile wynosi zagadkowa liczba:"
              ).grid(row = 2, column = 0)
        self.ent_numb = Entry(self, width = 5)
        self.ent_numb.grid(row = 2, column = 1)

        self.bttn2 = Button(self, text = "Sprawdz", command = self.check_number)
        self.bttn2.grid(row = 3, column = 1)


        Label(self,
              text = "Wynik:"
              ).grid(row = 4, column = 0, sticky = E)
        self.text_box2 = Text(self, width = 10, height = 1)
        self.text_box2.grid(row = 4, column = 1)

        Label(self,
              text = "Ilosc prob:"
              ).grid(row = 5, column = 0, sticky = E)
        self.text_box3 = Text(self, width = 5, height = 1)
        self.text_box3.grid(row = 5, column = 1)

        self.text_box4 = Text(self, width = 10, height = 1)
        self.text_box4.grid(row = 6, column = 1, columnspan = 2)

    def check_number(self):

        x = int(self.ent_numb.get())
        y = int(self.number)
        message = ""
        if x < y:
            message = "ZA MALO"
        elif x > y:
            message = "ZA DUZO"
        elif x == y:
            message = "ZGADLES"


        self.tries += 1
        self.text_box3.delete(0.0, END)
        self.text_box3.insert(0.0, str(self.tries))
        self.text_box2.delete(0.0, END)
        self.text_box2.insert(0.0, message)



    def draw_number(self):

        self.number = random.randint(0,10)
        self.tries = 0
        self.text_box3.delete(0.0, END)
        self.text_box2.delete(0.0, END)
        """
        message = str(self.number) + " " + str(self.tries)
        self.text_box4.delete(0.0, END)
        self.text_box4.insert(0.0, message)
        """


root = Tk()
root.title("Jaka to liczba")
root.geometry("300x200")

app = Application(root)

root.mainloop()