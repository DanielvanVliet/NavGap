import csv
import os
import time
import tkinter
import subprocess
#import commands

#from dijkstra algorithm
routeList = []
global tempcounter
tempcounter = 1
#spotdict name : [connection, strength, loc X, loc Y], node gets appended behind it once the script starts
spotDict = {
    'RPI_AP2' : [False, 0, 50, 150],
    'Connectify-me' : [False, 0, 180, 90],
    'RPI_AP1' : [False, 0, 50, 50],
    'RPI_AP3' : [False, 0, 50 , 250]
}

connectDict = {
    'RPI_AP2' : ['Connectify-me', 'RPI_AP1'],
    'Connectify-me' : ['RPI_AP2', 'RPI_AP1', 'RPI_AP3'],
    'RPI_AP3' : ['RPI_AP2', 'Connectify-me'],
    'RPI_AP1' : ['RPI_AP2', 'Connectify-me']
}

userList = []

## updates the list of connections ##
def updateList():
    global spotDict
    global userList
    print('# update list #')
    updateCmd = 'sudo iwlist wlan0 scan |grep -e Signal -e ESSID'

    trueCount = 0
    ## use this when testing on pi
    # result = subprocess.getoutput(updateCmd)
    # if len(result) > 0:
    #     userList = []
    #     for spot in spotDict:
    #         row = 0
    #         for line in result.split('\n'):
    #             row += 1
    #             essid = line[27:-1]
    #             signal = line[49:51]
    #             #print(essid)
    #             #print(signal)
    #             if row % 2 == 1:
    #                 rowdata = signal
    #                 #print(rowdata)
    #             if essid == spot and int(rowdata) <= 70: # -75 = range limiter
    #                 print('{} set to true, breaking for loop, current str: {}'.format(essid, rowdata))
    #                 spotDict[spot][0] = True
    #                 spotDict[spot][1] = rowdata
    #                 userList.append(essid)
    #                 break
    #             else:
    #                 if spotDict[spot][0] == True and essid == spot:
    #                     print('{} set to false, last str: {}'.format(essid, rowdata))
    #                 spotDict[spot][0] = False
    #                 #print('{} set to false'.format(essid))
    # print('user inbetween: {}'.format(userList))

    # this is for pc testing, rips info from old log
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
                if essid == spot and int(rowdata) <= 70: # range limiter
                    print('{} set to true, breaking for-loop'.format(essid))
                    spotDict[spot][0] = True
                    spotDict[spot][1] = rowdata
                    userList.append(essid)
                    break
                else:
                    spotDict[spot][0] = False
                    #print('{} set to false'.format(essid))



## GUI ##
blue = '#08088A'
yellow = '#FFFF00'
red = '#FF0000'
green = '#3ADF00'
running = False

def createOval(canvas, spotName, x, y):
    ovalSize = 8
    print('creating {} (node) on {} at {}, {}'.format(spotName, canvas, x, y))
    nodeLoc = [
        [(x-ovalSize), (y-ovalSize)],
        [(x+ovalSize), (y+ovalSize)]
    ]
    create = canvas.create_oval(nodeLoc[0][0], nodeLoc[0][1], nodeLoc[1][0], nodeLoc[1][1], fill=blue, activefill=red)
    createLabel = canvas.create_text(x, (y+20), text=spotName)
    global spotDict
    spotDict[spotName].append([create, createLabel, x, y])

#def createLabel(canvas, spotName, x, y)

def createUser(canvas, x, y):
    ovalSize = 4
    print('creating (solo node) at {}, {}'.format(x, y))
    nodeLoc = [
        [(x-ovalSize), (y-ovalSize)],
        [(x+ovalSize), (y+ovalSize)]
    ]
    global user
    user = canvas.create_oval(nodeLoc[0][0], nodeLoc[0][1], nodeLoc[1][0], nodeLoc[1][1], fill=green, activefill=red)

def createConnection(canvas, point1, point2):
    # (x1, y1, x2, y2)
    print('creating connection between {} at x{},y{} and {} at x{},y{}'.format(point1,
                                                                               spotDict[point1][2], spotDict[point1][3],
                                                                               point2,
                                                                               spotDict[point2][2], spotDict[point2][3]))
    canvas.create_line(spotDict[point1][2], spotDict[point1][3], spotDict[point2][2], spotDict[point2][3])

def createRoute(canvas, point1, point2, color):
    # (x1, y1, x2, y2)
    print('creating connection between {} at x{},y{} and {} at x{},y{}'.format(point1,
                                                                               spotDict[point1][2], spotDict[point1][3],
                                                                               point2,
                                                                               spotDict[point2][2], spotDict[point2][3]))
    line = canvas.create_line(spotDict[point1][2], spotDict[point1][3], spotDict[point2][2], spotDict[point2][3], fill=color)
    routeList.append(line)

def routeLiner(canvas, path):
    print("Lining Path")
    counter = 0
    for each in path:
        if counter < len(path)-1:
            print('create path between {} and {}'.format(path[counter], path[counter+1]))
            createRoute(canvas, path[counter], path[counter+1], red)
        counter += 1

#triangulation (pseudo)
def updateUser(canvas, user, points):
    xCoords = []
    yCoords = []

    for each in points:
        #print(each)
        #print(spotDict[each][2], spotDict[each][3])
        xCoords.append(spotDict[each][2])
        yCoords.append(spotDict[each][3])

    sumDif = 0
    counter = 0
    for each in xCoords:
        if counter < len(xCoords)-1:
            if xCoords[counter] > xCoords[counter+1]:
                sumDif = xCoords[counter] - xCoords[counter+1]
                xCoords[counter+1] = xCoords[counter] - sumDif /2
                counter += 1
            else:
                xCoords[counter+1] - xCoords[counter]
                xCoords[counter+1] = xCoords[counter+1] - sumDif /2
                counter +=1

    sumDif = 0
    counter = 0
    for each in yCoords:
        if counter <len(yCoords)-1:
            if yCoords[counter] > yCoords[counter+1]:
                sumDif = yCoords[counter] - yCoords[counter+1]
                yCoords[counter+1] = yCoords[counter] - sumDif /2
                counter += 1
            else:
                yCoords[counter+1] - yCoords[counter]
                yCoords[counter+1] = yCoords[counter+1] - sumDif /2
                counter +=1

    #print(xCoords[-1])
    #print(yCoords[-1])


    ovalSize = 4
    nodeLoc = [
        [(xCoords[-1])-ovalSize, (yCoords[-1])-ovalSize],
        [(xCoords[-1])+ovalSize, (yCoords[-1])+ovalSize]
    ]
    #print(nodeLoc)
    canvas.coords(user, nodeLoc[0][0], nodeLoc[0][1], nodeLoc[1][0], nodeLoc[1][1])


    #canvas.coords(user, xCoords[-1], yCoords[-1])

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

##### DIJKSTRA ALGORITHM #####
def dijkstra(graph_dict, start, end):
    print("Graph used: ",graph_dict)
    # create empty dictionary to hold the distance of each node to the start node
    distances = {}

    # create empty dict to hold the predecessor of each node
    predecessors = {}

    # set all initial distances to infinity
    #  and no predecessor for any node
    for node in graph_dict:
        distances[node] = float('inf')
        predecessors[node] = None
    print()
    # create empty list for nodes that have been visited with permanent distance
    labelled_nodes = []

    # set the distance from the start node to be 0
    distances[start] = 0

    # as long as there are still nodes to assess:
    while len(labelled_nodes) < len(graph_dict):

        # create empty dict for nodes that are still available
        still_in = {}
        for node in graph_dict:
            if node not in labelled_nodes:
                still_in[node] = distances[node]

        # find the node with the lowest distance to the current node
        lowest = float('inf')
        for each in still_in:
            if still_in.get(each) < lowest:
                lowest = still_in.get(each)
                closest = each
        # and add it to the permanently labelled nodes
        labelled_nodes.append(closest)

        # if node is a neighbor of closest
        for node in graph_dict[closest]:
            if graph_dict[closest].get(node) != None:
                # if a shorter path to that node can be found
                if distances[node] > distances[closest] + graph_dict[closest].get(node):
                # update the distance with that shorter distance
                    distances[node] = distances[closest] + graph_dict[closest].get(node)
                # set the predecessor for that node
                    predecessors[node] = closest

    path = [end]
    while start not in path:
        path.append(predecessors[path[-1]]) #find and append the predecessor of the last node in path
    # return the path
    return path[::-1]

##### UI LOOP #####
def createUI():
    print('# creating UI #')
    running = True
    WIDTH, HEIGHT = 420, 300
    root = tkinter.Tk()
    bgImage = tkinter.PhotoImage(file='background.gif')
    canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()

    background = canvas.create_image((WIDTH/2),(HEIGHT/2), image=bgImage)
    #root.overrideredirect(True)
    #root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    for con in connectDict:
        for link in connectDict[con]:
            createConnection(canvas, con, link)

    for each in spotDict:
        print(each)
        createOval(canvas, each, spotDict[each][2], spotDict[each][3])

    exit = tkinter.Button(text='exit', command=lambda :stopApp(root))
    exit_place = canvas.create_window(20, 30, window=exit)

    createUser(canvas, WIDTH/2, HEIGHT/2)
    counter = 0

    while running:
        if counter > 500:
            updateList()
            counter = -1
            time.sleep(0.1)
            updateUser(canvas,user, userList)

        updateNodes(canvas)
        #if endlocation is given somehow, run Dijkstra_Algorithm, path returned has to be given to routeLiner(canvas, path) and run ONCE
        global tempcounter
        if tempcounter != 0:
            routeLiner(canvas, ['RPI_AP3', 'RPI_AP2', 'Connectify-me']) #run this once
            tempcounter -=1

        root.update_idletasks()
        root.update()
        counter += 1


## app boot loop ##
while True:
    print('running on {}'.format(os.name)) # windows = nt, rpi = posix
    updateList()
    print(spotDict)
    text = input(' | null = update list \n | break = nuke app \n | start = start app \n >')
    if text == 'break':
        break
    elif text == 'start':
        createUI()
