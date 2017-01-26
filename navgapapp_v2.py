import csv
import os
import time
import tkinter


#spotdict name : [connection, strength, loc X, loc Y]
spotDict = {
    'RPI_AP2' : [False, 0, 90, 180],
    'Connectify-me' : [False, 0, 50, 70],
    'tempMichelLoc' : [False, 0, 220, 50],
    'NogEenTest' : [False, 0, 230, 250]
}

connectDict = {
    'RPI_AP2' : 'Connectify-me',
    'RPI_AP2' : 'tempMichelLoc',
    'Connectify-me' : 'NogEenTest',
    'tempMichelLoc' : 'NogEenTest',
    'tempMichelLoc' : 'Connectify-me'
}


## update essidList ##
updateCmd = 'sudo bash /home/pi/github/NavGap/navgapboot.sh start'
# look for a way to make this less heavy for the system by dropping the logging into .csv and recording directly into python
# currently the Cmd to log and load is too heavy for the system
# http://stackoverflow.com/questions/4760215/running-shell-command-from-python-and-capturing-the-output

def updateList():
    global spotDict
    essidList = []
    signalList = []
    print('# update list #')
    #os.system(updateCmd)

    for spot in spotDict:
        print(' | Connection: {:15}: {}, strength: {}'.format(spot, spotDict[spot][0], spotDict[spot][1]))
        with open('log.csv', 'r') as file:
            reader = csv.reader(file)
            row = 0
            for line in reader:
                row += 1
                essid = line[0][27:-1]
                signal = line[0][49:51]
                #print(spot)
                #print(essid)
                if row % 2 == 1:
                    rowdata = signal
                    #print(rowdata)
                if essid == spot and int(rowdata) <= 75: # -75 = range limiter
                    print('{} set to true, breaking for loop'.format(essid))
                    spotDict[spot][0] = True
                    spotDict[spot][1] = rowdata
                    break
                else:
                    spotDict[spot][0] = False
                    #print('{} set to false'.format(essid))


## GUI ##
blue = '#08088A'
yellow = '#FFFF00'
red = '#FF0000'
running = False

def createOval(canvas, spotName, x, y):
    ovalSize = 8
    print('creating {} (node) on {} at {}, {}'.format(spotName, canvas, x, y))
    nodeLoc = [
        [(x-ovalSize), (y-ovalSize)],
        [(x+ovalSize), (y+ovalSize)]
    ]
    create = canvas.create_oval(nodeLoc[0][0], nodeLoc[0][1], nodeLoc[1][0], nodeLoc[1][1], fill=blue, activefill=red)
    global spotDict
    #nodeDict[nodeName] = [create, x, y]
    spotDict[spotName].append([create, x, y])

def createConnection(canvas, point1, point2):
    # (x1, y1, x2, y2)
    canvas.create_line(spotDict[point1][2], spotDict[point1][3], spotDict[point2][2], spotDict[point2][3])

def changeNodeColor(canvas, spotName, color):
    canvas.itemconfig(spotDict[spotName][-1][0], fill=color)

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
            changeNodeColor(canvas, each, yellow)
        else:
            changeNodeColor(canvas, each, blue)

def createUI():
    print('# creating UI #')
    running = True
    WIDTH, HEIGHT = 420, 300
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()

    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    for con in connectDict:
        createConnection(canvas, con, connectDict[con])

    for each in spotDict:
        print(each)
        createOval(canvas, each, spotDict[each][2], spotDict[each][3])

    exit = tkinter.Button(text='exit', command=lambda :stopApp(root))
    exit_place = canvas.create_window(20, 30, window=exit)

    counter = 0
    while running:
        if counter > 1000:
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
    print(spotDict)
