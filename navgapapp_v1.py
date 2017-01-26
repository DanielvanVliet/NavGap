import csv
import os
import time
import tkinter

spotList = {
    'Connectify-me' : [False, 0],
    'RPI_AP2' : [False, 0]
}

## update essidlist ##
EssidList = []
SignalList = []
tempList = {}
updateCmd = 'sudo bash /home/pi/github/NavGap/navgapboot.sh start'

def updateList():
    global EssidList
    global SignalList
    global tempList
    EssidList = []
    SignalList = []
    print('# update list #')
    os.system(updateCmd)
    with open('log.csv', 'r') as file:
        reader = csv.reader(file)
        row = 0
        for each in reader:
            row += 1
            if row % 2 == 1:
                SignalList.append(each[0][48:51])
            else:
                EssidList.append(each[0][27:-1])

    # for essid in SignalList:
    #     tempList.append([essid])
    # counter = 0
    # for signal in EssidList:
    #     tempList[counter].append(signal)
    #     counter +=1

    counter = 0

    for essid in EssidList:
        #print('{} in EssidList'.format(essid))
        if essid in spotList:
            #print('{} in spotList'.format(essid))
            tempList[essid] = SignalList[counter]
        counter += 1


## GUI ##
blue = '#08088A'
yellow = '#FFFF00'
red = '#FF0000'
running = False

def changeNodeColor(canvas, node, color):
    print('{} node changed color: {}'.format(node, color))
    canvas.itemconfig(node, fill=color)

def stopApp(tkroot):
    print('killing root')
    running = False
    tkroot.destroy()
    tkroot.quit()


def createUI():
    print('# creating UI #')
    running = True
    WIDTH, HEIGHT = 420, 300
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.grid()

    # drawing test ovals
    x0, y0 = 10, 50
    x1, y1 = 50, 90
    x2, y2 = 90, 130

    o1 = canvas.create_oval(x0, x0, y0, y0, fill=blue, activefill=red)
    o2 = canvas.create_oval(x1, x1, y1, y1, fill=blue, activefill=red)
    o3 = canvas.create_oval(x2, x2, y2, y2, fill=blue, activefill=red)

    exit = tkinter.Button(text='exit', command=lambda :stopApp(root))
    exit.grid()

    while running:
        root.update_idletasks()
        root.update()


## app Loop ##
while True:
    text = input('{null = update list \n | break = nuke app \n | start = start app}')
    if text == 'break':
        break
    elif text == 'start':
        createUI()

    updateList()
    print(tempList)
