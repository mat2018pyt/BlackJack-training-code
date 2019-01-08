from tkinter import *

class Application(Frame):

    def __init__(self, master):

        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        self.bttn1 = Button(self, text = "Nic nie robię")
        self.bttn1.grid()

        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text = "Nie działam")

        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "Ja też"

root = Tk()
root.title("Leniwe przyciski 2")
root.geometry("300x200")

ramka = Application(root)

root.mainloop()

