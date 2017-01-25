from tkinter import *
#schermresolutie is 420x300
def gaan():
    print('Doe hier de functie')

def check(var, entry):
    if len(var) is not 1:
        if entry == 'entry_1':
            entry_1.delete(0, END)
        if entry == 'entry_2':
            entry_2.delete(0, END)
    else:
        print('{} is goed'.format(var))

def callback():
    beginlocatie = entry_1.get().lower()
    eindlocatie = entry_2.get().lower()
    print('{}\n{}'.format(beginlocatie, eindlocatie))
    check(beginlocatie, 'entry_1')
    check(eindlocatie, 'entry_2')

    if beginlocatie=='a' and eindlocatie=='b':
        photo1 = PhotoImage(file="Kaart IDP ab.gif")
        label = Label(image=photo1)
        label.image = photo1 # keep a reference
        label.grid(row=3, column=1)

    elif beginlocatie=='a' and eindlocatie=='c':
        photo2 = PhotoImage(file="Kaart IDP ac.gif")
        label = Label(image=photo2)
        label.image = photo2
        label.grid(row=3, column=1)

    elif beginlocatie=='a' and eindlocatie=='d':
        photo3 = PhotoImage(file="Kaart IDP ad.gif")
        label = Label(image=photo3)
        label.image = photo3
        label.grid(row=3, column=1)

root = Tk()

WIDTH, HEIGHT = 475, 280
label = Canvas(root, width=WIDTH, height=HEIGHT, bg="green")
label.grid(row=0, column=0, sticky=NW)

label_1 = Label(root, text="Beginlocatie")
label_2 = Label(root, text="Eindlocatie")

entry_1 = Entry(root) #Lege ruimte om iets in te vullen
entry_1.delete(0, END)

entry_2 = Entry(root)
entry_2.delete(0, END)

label_1.grid(row=0, column=0, sticky=NW)     #Met sticky zeg je aan welke kant je het wilt, N,E,S,W (north,east,south,west)
label_2.grid(row=1, column=0, sticky=NW)     #Met grid zeg je waar het moet staan, soort van excel

entry_1.grid(row=0, column=1, sticky=NW)
entry_2.grid(row=1, column=1, sticky=NW)

button1 = Button(root, text="Gaan!", command=callback, fg="white", bg="black")
button1.grid(row=2, sticky=E)

photo = PhotoImage(file="Kaart IDP neutraal.gif")
label = Label(image=photo)
label.image = photo # keep a reference!

root.mainloop()
