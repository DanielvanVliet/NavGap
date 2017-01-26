import csv
import os
import time
import tkinter

spotDict = {
    'RPI_AP2' : [False, 0]
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
        with open('log.csv', 'r') as file:
            reader = csv.reader(file)
            row = 0
            print('##checking spot##')
            print(spot)
            for line in reader:
                #print(line)
                row += 1
                #print(spot)
                #print(line[0][27:-1])
                if row % 2 == 1:
                    rowdata = line[0][48:51]
                    #print(rowdata)
                elif spot == line[0][27:-1]:
                    print('####################')
                    print('{} == {}'.format(line[0][27:-1], spot))
                    #print(line[0][27:-1])
                    spotDict[line[0][27:-1]][0] = True
                    spotDict[line[0][27:-1]][1] = rowdata
                    print(spot, 'set to true, breaking for-loop')
                    break
                elif line[0][27:-1] in spotDict:
                    print('set to false')
                    spotDict[line[0][27:-1]][0] = False


        # for each in reader:
        #     #print(each)
        #     row += 1
        #     if row % 2 == 1:
        #         #signalList.append(each[0][48:51])
        #         rowdata = each[0][48:51]
        #         #print(rowdata)
        #     elif each[0][27:-1] in spotDict:
        #         #essidList.append(each[0][27:-1])
        #         spotDict[each[0][27:-1]][0] = True
        #         spotDict[each[0][27:-1]][1] = rowdata


    # for essid in signalList:
    #     tempDict.append([essid])
    # counter = 0
    # for signal in essidList:
    #     tempDict[counter].append(signal)
    #     counter +=1

    counter = 0

    # for essid in essidList:
    #     #print('{} in essidList'.format(essid))
    #     if essid in spotDict:
    #         #print('{} in spotDict'.format(essid))
    #         #tempDict[essid] = signalList[counter]
    #         spotDict[essid] = [True, signalList[counter]]
    #         #spotDict[essid][0] = False
    #     counter += 1

    # for spot in spotDict:
    #     if spot in tempDict:
    #         print(spot, 'turning spot on')
    #         spotDict[spot][0] = True
    #         spotDict[spot][1] = tempDict[spot]
    #     else:
    #         print(spot, 'turning spot off')
    #         spotDict[spot][0] = False


## GUI ##
blue = '#08088A'
yellow = '#FFFF00'
red = '#FF0000'
running = False

coordA = [90, 180]
coordB = [50, 70]
coordC = [120, 200]
ovalSize = 8

# def createOval(coord):
#     global node
#     tempCoord = coord.copy()
#     tempCoord1 = coord.copy()
#     node = [[], []]
#     counter = 0
#     for each in coord:
#         if counter == 0:
#             tempCoord[0] -= ovalSize
#             node[0].append(tempCoord[0])
#             tempCoord[1] -= ovalSize
#             node[0].append(tempCoord[1])
#             counter += 1
#         else:
#             tempCoord1[0] += ovalSize
#             node[1].append(tempCoord1[0])
#             tempCoord1[1] += ovalSize
#             node[1].append(tempCoord1[1])

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
    #print('{} node changed color: {}'.format(node, color))
    #canvas.itemconfig(node, fill=color)
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

    # drawing test ovals
    # x0, y0 = 10, 50
    # x1, y1 = 50, 90
    # x2, y2 = 90, 130
    #
    # o1 = canvas.create_oval(x0, x0, y0, y0, fill=blue, activefill=red)
    # o2 = canvas.create_oval(x1, x1, y1, y1, fill=blue, activefill=red)
    # o3 = canvas.create_oval(x2, x2, y2, y2, fill=blue, activefill=red)
    #o3switch = False

    createOval(canvas, 'nodeA', 20, 50)

    exit = tkinter.Button(text='exit', command=lambda :stopApp(root))
    exit_place = canvas.create_window(10, 10, window=exit)

    counter = 0
    print(nodeDict)
    while running:
        if counter > 100000:
            updateList()
            counter = -1

        updateNodes(canvas)
        root.update_idletasks()
        root.update()
        counter += 1

## app Loop ##
while True:
    text = input(' | null = update list \n | break = nuke app \n | start = start app \n ')
    if text == 'break':
        break
    elif text == 'start':
        createUI()

    #createUI()
    updateList()
    print(tempDict)
    print(spotDict)
