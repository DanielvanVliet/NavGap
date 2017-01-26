import time
import tkinter
#coords between (10,10) and (415, 295), otherwise it won't be drawn ON the canvas
coordA = [230, 44]
coordB = [145, 80]

def createOval(coord):
    global node
    tempCoord = coord.copy()
    tempCoord1 = coord.copy()
    node = [[], []]
    counter = 0
    for each in coord:
        if counter == 0:
            tempCoord[0] -= 5
            node[0].append(tempCoord[0])
            tempCoord[1] -= 5
            node[0].append(tempCoord[1])
            counter += 1
        else:
            tempCoord1[0] += 5
            node[1].append(tempCoord1[0])
            tempCoord1[1] += 5
            node[1].append(tempCoord1[1])


blue = '#08088A'
yellow = '#FFFF00'
red = '#FF0000'

def createUI():
    base = tkinter.Tk()
    WIDTH = 420
    HEIGHT = 300
    canvas = tkinter.Canvas(base, width=WIDTH, height=HEIGHT)
    canvas.grid()

    createOval(coordA)
    o = canvas.create_oval(node[0][0], node[0][1], node[1][0], node[1][1], fill=blue, activefill=red)

    createOval(coordB)
    o1 = canvas.create_oval(node[0][0], node[0][1], node[1][0], node[1][1], fill=blue, activefill=red)
    o2 = canvas.create_line(coordB[0], coordB[1], coordA[0], coordA[1])
    #o3 = canvas.create_line(coordA[0], coordA[1], coordB[0], coordB[1])
    #createOval(coordC)
    #o3 = canvas.create_oval(node[0][0], node[0][1], node[1][0], node[1][1], fill=blue, activefill=red)

    base.mainloop()







createUI()
