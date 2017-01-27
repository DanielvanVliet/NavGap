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

root = Tk() #Tk() is de window

WIDTH, HEIGHT = 475, 280 #Grootte van het groene canvas
label = Canvas(root, width=WIDTH, height=HEIGHT, bg="green") #Dit is de canvas
label.grid(row=6, column=6, sticky=NW) #Plaatsing canvas

menu = Menu(root) #Aanmaken van de widget voor dropdown, geplaatst in de window
root.config(menu=menu)

locatie= Menu(menu)
menu.add_cascade(label="Locatie", menu=locatie) #Dit is de dropdown voor locatie
locatie.add_command(label="A", command=a1) #Optie 1 in de dropdown voor locatie
locatie.add_command(label="B", command=b1) #Optie 2 in de dropdown voor locatie

bestemming = Menu(menu)
menu.add_cascade(label="Bestemming", menu=bestemming) #Dit is de dropdown voor bestemming
bestemming.add_command(label="A", command=a2) #Optie 1 in de dropdown bestemming
bestemming.add_command(label="B", command=b2) #Optie 2 in de dropdown bestemming

button1 = Button(root, text="Gaan!", command=gaan, fg="white", bg="black") #Dit is de Gaan knop
button1.grid(row=2, sticky=E) #Plaatsing van de knop


root.mainloop() #Dit zorgt ervoor dat het programma blijft runnen
