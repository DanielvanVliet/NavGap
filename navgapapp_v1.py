import csv
import os
import time
import tkinter

spotList = {
    'Connectify-me' : [False, 0],
    'RPI_AP2' : [False, 0]
}

## update essidList ##
essidList = []
signalList = []
tempList = {}
updateCmd = 'sudo bash /home/pi/github/NavGap/navgapboot.sh start'

def updateList():
    global spotList
    global essidList
    global signalList
    global tempList
    essidList = []
    signalList = []
    print('# update list #')
    os.system(updateCmd)
    with open('log.csv', 'r') as file:
        reader = csv.reader(file)
        row = 0
        for each in reader:
            #print(each)
            row += 1
            if row % 2 == 1:
                #signalList.append(each[0][48:51])
                rowdata = each[0][48:51]
                #print(rowdata)
            else:
                #essidList.append(each[0][27:-1])
                tempList[each[0][27:-1]] = rowdata

    # for essid in signalList:
    #     tempList.append([essid])
    # counter = 0
    # for signal in essidList:
    #     tempList[counter].append(signal)
    #     counter +=1

    counter = 0

    # for essid in essidList:
    #     #print('{} in essidList'.format(essid))
    #     if essid in spotList:
    #         #print('{} in spotList'.format(essid))
    #         #tempList[essid] = signalList[counter]
    #         spotList[essid] = [True, signalList[counter]]
    #         #spotList[essid][0] = False
    #     counter += 1

    for spot in spotList:
        if spot in tempList:
            spotList[spot][0] = True
            spotList[spot][1] = tempList[spot]
        else:
            spotList[spot][0] = False


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
    canvas.pack()

    # drawing test ovals
    x0, y0 = 10, 50
    x1, y1 = 50, 90
    x2, y2 = 90, 130

    o1 = canvas.create_oval(x0, x0, y0, y0, fill=blue, activefill=red)
    o2 = canvas.create_oval(x1, x1, y1, y1, fill=blue, activefill=red)
    o3 = canvas.create_oval(x2, x2, y2, y2, fill=blue, activefill=red)

    #o3switch = False

    exit = tkinter.Button(text='exit', command=lambda :stopApp(root))
    exit_place = canvas.create_window(10, 10, window=exit)

    while running:
        time.sleep(1)
        updateList()
        for spot in spotList:
            if spot == 'RPI_AP2':
                print(spotList[spot])
                if spotList[spot][0] == True:
                    print('turn o3 on')
                    changeNodeColor(canvas, o3, yellow)
                elif spotList[spot][0] == False:
                    print('turn o3 off')
                    changeNodeColor(canvas, o3, blue)

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
    print(spotList)
