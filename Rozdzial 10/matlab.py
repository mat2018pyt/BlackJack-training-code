from tkinter import *

class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text = "Wprowadz informacje do nowego opowiadania"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
        Label(self,
              text = "Osoba: "
              ).grid(row = 1, column = 0, sticky = W)
        Label(self,
              text = "Rzeczownik w liczbie mnogiej: "
              ).grid(row = 2, column = 0, sticky = W)
        Label(self,
              text = "Czasownik: "
              ).grid(row = 3, column = 0, sticky = W)
        Label(self,
              text = "Przymiotnik(i): "
              ).grid(row = 4, column = 0, sticky = W)
        Label(self,
              text = "Czesc ciala: "
              ).grid(row = 5, column = 0, sticky = W)

        self.bttn = Button(self,
                           text = "Kliknij, aby wyswietlic opowiadanie",
                           command = self.update_text
                           )
        self.bttn.grid(row = 6, column = 0, sticky = W)

        self.text_box = Text(self, width = 75, height = 10, wrap = WORD)
        self.text_box.grid(row = 7, column = 0, columnspan = 4)

        self.person_text = Entry(self)
        self.person_text.grid(row = 1, column = 1, sticky = W)

        self.noun_text = Entry(self)
        self.noun_text.grid(row = 2, column = 1, sticky = W)

        self.verb_text = Entry(self)
        self.verb_text.grid(row = 3, column = 1, sticky = W)

        self.is_checked1 = BooleanVar()
        Checkbutton(self,
                    text = "naglace",
                    variable = self.is_checked1,
                    ).grid(row = 4, column = 1, sticky = W)

        self.is_checked2 = BooleanVar()
        Checkbutton(self,
                    text = "radosne",
                    variable = self.is_checked2,
                    ).grid(row = 4, column = 2, sticky = W)

        self.is_checked3 = BooleanVar()
        Checkbutton(self,
                    text = "elektryzujace",
                    variable = self.is_checked3,
                    ).grid(row = 4, column = 3, sticky = W)

        self.body_parts = StringVar()
        self.body_parts.set(None)

        body_parts = ["pepek", "duzy palec u nogi", "rdzen przedluzony"]
        column = 1

        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_parts,
                        value = part
                        ).grid(row = 5, column = column, sticky = W)
            column += 1





    def update_text(self):
        person = self.person_text.get()
        noun = self.noun_text.get()
        verb = self.verb_text.get()
        adjectives = ""
        if self.is_checked1.get():
            adjectives += "naglace, "
        if self.is_checked2.get():
            adjectives += "radosne, "
        if self.is_checked3.get():
            adjectives += "elektrzujace, "
        body_part = self.body_parts.get()

        story = "Sławny badacz i odkrywca "
        story += person
        story += " o mało co nie zrezygnował z życiowej misji poszukiwania "
        story += "zaginionego miasta, które zamieszkiwały "
        story += noun
        story += ", gdy pewnego dnia "
        story += noun
        story += " znalazły "
        story += person + "a. "
        story += "Silne, "
        story += adjectives
        story += "osobliwe uczucie owładnęło badaczem. "
        story += "Po tak długim czasie poszukiwanie wreszcie się zakończyło. W oku "
        story += person + "a pojawiła się łza, która spadła na jego "
        story += body_part + ". "
        story += "A wtedy "
        story += noun
        story += " szybko pożarły "
        story += person + "a. "
        story += "Jaki morał płynie z tego opowiadania? Pomyśl, zanim zaczniesz coś "
        story += verb
        story += "."

        self.text_box.delete(0.0, END)
        self.text_box.insert(0.0, story)


root = Tk()
root.title("Mad Lib")

app = Application(root)

root.mainloop()


