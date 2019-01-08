from tkinter import *

root = Tk()

root.title("Prosty interfejs GUI")
root.geometry("600x400")

app = Frame(root)
app.grid()

lbl = Label(app, text = "Czesc Bonka !!! Czesc Rico !!!")
lbl.grid()

but = Button(root)
but.grid()


root.mainloop()





