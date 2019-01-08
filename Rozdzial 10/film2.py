from tkinter import *

class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
             text = "Wybierz swoj ulubiony gatunek filmu"
             ).grid(row = 0, column = 0, sticky = W)


        self.lbl2 = Label(self, text = "Wybierz jeden gatunek:")
        self.lbl2.grid(row = 1, column = 0, sticky = W)

        self.favorite = StringVar()
        self.favorite.set(None)

        Radiobutton(self,
                    text = "komedia",
                    variable = self.favorite,
                    value = "komedia.",
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)

        Radiobutton(self,
                    text = "dramat",
                    variable = self.favorite,
                    value = "drama.",
                    command = self.update_text
                    ).grid(row = 3, column = 0, sticky = W)

        Radiobutton(self,
                    text = "romans",
                    variable = self.favorite,
                    value = "romans.",
                    command = self.update_text
                    ).grid(row = 4, column = 0, sticky = W)

        self.textbox = Text(self, width = 40, height = 5, wrap = WORD)
        self.textbox.grid(row = 5, column = 0, columnspan = 3)

    def update_text(self):

        message = "Twoim ulubionym gatunkiem filmu jest: "
        message += self.favorite.get()

        self.textbox.delete(0.0, END)
        self.textbox.insert(0.0, message)


root = Tk()
root.title("Wybur filmow 2")
app = Application(root)
root.mainloop()




