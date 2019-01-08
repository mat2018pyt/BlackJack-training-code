from tkinter import *

class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.widgets_create()

    def widgets_create(self):
        self.inst_lbl = Label(self, text = "Wprowadz haslo do sekretu dlugowiecznosci")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        self.pw_lbl = Label(self, text = "Haslo: ")
        self.pw_lbl.grid(row = 1, column = 0, sticky = W)

        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)

        self.bttn1 = Button(self, text = "Akceptuj", command = self.reveal)
        self.bttn1.grid(row = 2, column = 0, sticky = W)

        self.secret_txt = Text(self, width = 35, height  = 5, wrap = WORD)
        self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)


    def reveal(self):
        contents = self.pw_ent.get()
        if contents == "sekret":
            message = "Oto tajemny przepis na dożycie 100 lat: dożyj 99 lat, " \
                      "a potem bądź BARDZO ostrożny."
        elif contents == "Bonka":
            message = "Kocham Cie najlepsza Bonko na Swiecie, moja wspaniala Aniu  !!!"
        else:
            message = "To nie jest poprawne hasło, więc nie mogę się z Tobą " \
                      "podzielić swoim sekretem."

        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)


root = Tk()
root.title("Dlugowiecznosc")
root.geometry("300x150")

app = Application(root)

root.mainloop()




























