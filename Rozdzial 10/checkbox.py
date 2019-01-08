from tkinter import *

class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        Label(self, text = "Wybierz swoje ulubione gatunki filmow.").grid(row = 0, column = 0, sticky = W)

        self.lbl2 = Label(self, text = "Zaznacz wszystkie, ktore chcialbys wybrac:")
        self.lbl2.grid(row = 1, column = 0, columnspan = 2, sticky = W)

        self.likes_commedy = BooleanVar()
        Checkbutton(self, text = "komedia", variable = self.likes_commedy, command = self.update_text).grid(row = 2, column = 0, sticky = W)

        self.likes_dramma = BooleanVar()
        Checkbutton(self, text = "dramat", variable = self.likes_dramma, command = self.update_text).grid(row = 3, column = 0, sticky = W)

        self.likes_romans = BooleanVar()
        Checkbutton(self, text = "romans", variable = self.likes_romans, command = self.update_text).grid(row = 4, column = 0, sticky = W)

        self.text = Text(self, width = 40, height = 5, wrap = WORD)
        self.text.grid(row = 5, column = 0, columnspan = 3, sticky = W)


    def update_text(self):
        likes = ""

        if self.likes_commedy.get():
            likes += "Lubisz filmy komiediowe\n"

        if self.likes_dramma.get():
            likes += "Lubisz filmy dramatyczne\n"

        if self.likes_romans.get():
            likes += "Lubisz filmy romantyczne\n"

        self.text.delete(0.0, END)
        self.text.insert(0.0, likes)





root = Tk()
root.title("Wybor filmow")
root.geometry("300x200")

app = Application(root)

root.mainloop()

