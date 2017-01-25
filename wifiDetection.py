import csv
import os
import time
import tkinter

conList = [
        'MarcKYS',
        'essidhere',
        'Connectify-me'
]
EssidList = []
SignalList = []
tlist = []
connection = False
updateCmd = 'sudo bash /home/pi/github/NavGap/navgapboot.sh start'

## UI Creation ##
#add current selected connection to curList, if signal strength is too low it gets cut off instead
#show all connections with whom user is connected
#Pick highest value loc in curList and triangulate location of user by reducing the x and y cordinates of user by that of the other location(s)
#Extra: signal strength adjusts the location further by pushing it to either side.

def createUI():
    blue = '#08088A'
    yellow = '#FFFF00'

    x0, y0 = 10, 50
    x1, y1 = 50, 90
    x2, y2 = 90, 130
    WIDTH = 420
    HEIGHT = 300
    base = tkinter.Tk()
    canvas = tkinter.Canvas(base, width=WIDTH, height=HEIGHT)
    canvas.grid()

    # (loc X, locY, x, y)
    o1 = canvas.create_oval(x0, x0, y0, y0, fill=blue, activefill=yellow)
    o2 = canvas.create_oval(x1, x1, y1, y1, fill=blue, activefill=yellow)
    o3 = canvas.create_oval(x2, x2, y2, y2, fill=blue, activefill=yellow)

    #canvas.create_oval()
    # STD stndard algoritme

    base.mainloop()
createUI()


## Algoritme ##
def checkConnection(essid):
        global connection
        for each in conList:
                #print('checking if {} is {}'.format(essid, each))
                if essid == each:
                        connection = True
                        #print('######## DICHTBIJ POINT {} #########'.format(essid))
                elif connection == False:
                        #print('## No Connection ##')
                        connection = False

#print('### updating log.csv ###')
#os.system(updateCmd)
counter = 1
#while True:
while counter != 0:
        time.sleep(0.1)
        #print('### Update ###')
        os.system(updateCmd)
        with open('log.csv', 'r') as myCSVFile:
                reader = csv.reader(myCSVFile)
                row = 0
                for each in reader:
                        #print(each)
                        row += 1
                        if row % 2 == 1: #if even
                                #print(each[0][48:52])
                                EssidList.append(each[0][48:51])
                        else:
                                #print(each[0][27:-2])
                                SignalList.append(each[0][27:-1])
                                checkConnection(each[0][27:-1])           
        counter -= 1

        for essid in SignalList:
                tlist.append([essid])                
        count = 0
        for signal in EssidList:
                tlist[count].append(signal)
                count +=1
        print('### temp list ###')
        print(tlist)
print()
print()
for each in tlist:
	print('{} : {}'.format(each[0],each[1]))


