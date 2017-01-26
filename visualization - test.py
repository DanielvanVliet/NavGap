import tkinter

coordA = [[150, 200], [200, 250]]

blue = '#08088A'
yellow = '#FFFF00'
red = '#FF0000'

def createUI():
    base = tkinter.Tk()
    WIDTH = 420
    HEIGHT = 300
    canvas = tkinter.Canvas(base, width=WIDTH, height=HEIGHT)
    canvas.grid()

    o = canvas.create_oval(coordA[0][0], coordA[0][1], coordA[1][0], coordA[1][1], fill=blue, activefill=red)

    base.mainloop()

createUI()
