from tkinter import *

root = Tk()
root.title("Leniwe przyciski")
root.geometry("400x300")


app = Frame(root)
app.grid()

btn1 = Button(app, text = "Przycisk 1")
btn1.grid()

btn2 = Button(app, text = "Przycisk 2")
btn2.grid()

btn3 = Button(app)
btn3.grid()
btn3.configure(text = "Przycisk 3")

btn4 = Button(app)
btn4.grid()

btn4["text"] = "Przycisk 4"







root.mainloop()