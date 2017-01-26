import csv
import os
import time
import tkinter


#spotdict name : [connection, strength]
spotDict = {
    'RPI_AP2' : [False, 0]
    #'Connectify-me' : [False, 0]
}
nodeDict = {}

## update essidList ##
essidList = []
signalList = []
tempDict = {}
updateCmd = 'sudo bash /home/pi/github/NavGap/navgapboot.sh start'

def updateList():
    global spotDict
    global essidList
    global signalList
    global tempDict
    essidList = []
    signalList = []
    print('# update list #')
    os.system(updateCmd)

    for spot in spotDict:
        print(' | Connection: {:15}: {}, strength: {}'.format(spot, spotDict[spot][0], spotDict[spot][1]))
        with open('log.csv', 'r') as file:
            reader = csv.reader(file)
            row = 0
            for line in reader:
                row += 1
                essid = line[0][27:-1]
                signal = line[0][48:51]
                #print(spot)
                #print(essid)
                if row % 2 == 1:
                    rowdata = signal
                    print(rowdata)
                if essid == spot:
                    print('{} set to true, breaking for loop'.format(essid))
                    spotDict[spot][0] = True
                    spotDict[spot][1] = rowdata
                    break
                else:
                    spotDict[spot][0] = False
                    print('{} set to false'.format(essid))


    #for spot in spotDict:

## GUI ##
blue = '#08088A'
yellow = '#FFFF00'
red = '#FF0000'
running = False

coordA = [90, 180]
coordB = [50, 70]
coordC = [120, 200]
ovalSize = 8

def createOval(canvas, nodeName, x, y):
    print('creating {} (node) on {} at {}, {}'.format(nodeName, canvas, x, y))
    nodeLoc = [
        [(x-ovalSize), (y-ovalSize)],
        [(x+ovalSize), (y+ovalSize)]
    ]
    create = canvas.create_oval(nodeLoc[0][0], nodeLoc[0][1], nodeLoc[1][0], nodeLoc[1][1], fill=blue, activefill=red)
    global nodeDict
    nodeDict[nodeName] = [create, x, y]


def changeNodeColor(canvas, node, color):
    canvas.itemconfig(nodeDict[node][0], fill=color)

def stopApp(tkroot):
    print('killing root')
    running = False
    tkroot.destroy()
    tkroot.quit()

def updateNodes(canvas):
    for each in spotDict:
        #print(each)
        #print(spotDict[each][0])
        if spotDict[each][0] == True:
            changeNodeColor(canvas, 'nodeA', yellow)
        else:
            changeNodeColor(canvas, 'nodeA', blue)

def createUI():
    print('# creating UI #')
    running = True
    WIDTH, HEIGHT = 420, 300
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()

    createOval(canvas, 'nodeA', 20, 50)

    exit = tkinter.Button(text='exit', command=lambda :stopApp(root))
    exit_place = canvas.create_window(10, 10, window=exit)

    print(nodeDict)
    counter = 0
    while running:
        if counter > 10000:
            updateList()
            counter = -1

        updateNodes(canvas)
        root.update_idletasks()
        root.update()
        counter += 1

## app boot loop ##
while True:
    # text = input(' | null = update list \n | break = nuke app \n | start = start app \n ')
    # if text == 'break':
    #     break
    # elif text == 'start':
        #createUI()

    updateList()
    createUI()
    print(tempDict)
    print(spotDict)
