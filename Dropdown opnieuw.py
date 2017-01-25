from tkinter import *

locInvoer = ""
eindlocInvoer = ""
def a1():
    locInvoer = "A"
    print('Locatie = A')
def a2():
    eindlocInvoer = "A"
    print('Eindlocatie = A')
def b1():
    locInvoer = "B"
    print('Locatie = B')
def b2():
    eindlocInvoer = "B"
    print('Eindlocatie = B')
def gaan():
    print('MAAK HIER CODE VOOR!!!!!!!!!!!!!!!!1')

root = Tk()

WIDTH, HEIGHT = 475, 280
label = Canvas(root, width=WIDTH, height=HEIGHT, bg="green")
label.grid(row=6, column=6, sticky=NW)

menu = Menu(root)
root.config(menu=menu)

locatie= Menu(menu)
menu.add_cascade(label="Locatie", menu=locatie)
locatie.add_command(label="A", command=a1)
locatie.add_command(label="B", command=b1)
#locatie.add_separator()
#locatie.add_command(label="", command=doNothing())

bestemming = Menu(menu)
menu.add_cascade(label="Bestemming", menu=bestemming)
bestemming.add_command(label="A", command=a2)
bestemming.add_command(label="B", command=b2)

button1 = Button(root, text="Gaan!", command=gaan, fg="white", bg="black")
button1.grid(row=2, sticky=E)


root.mainloop()
