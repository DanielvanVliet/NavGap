import csv
import os
import time
import tkinter

conList = [
	'MarcKYS',
	'essidhere',
        'Connectify-me'
]
curList = []
tempList = []

connection = False
updateCmd = 'sudo /home/pi/github/NavGap/navgapboot.sh start'

def checkConnection(essid):
        global connection
        for each in conList:
                #print('checking if {} is {}'.format(essid, each))
                if essid == each:
                        connection = True
                        curList.append(essid)
                        print('######## DICHTBIJ POINT {} #########'.format(essid))
                elif connection == False:
                        print('## No Connection ##')

#add current selected connection to curList, if signal strength is too low it gets cut off instead
#show all connections with whom user is connected
#Pick highest value loc in curList and triangulate location of user by reducing the x and y cordinates of user by that of the other location(s)
#Extra: signal strength adjusts the location further by pushing it to either side.

def createUI():
    blue = '#08088A'
    yellow = '#FFFF00'
    WIDTH = 420
    HEIGHT = 300
    OVAL = 100
    base = tkinter.Tk()
    canvas = tkinter.Canvas(base, width=WIDTH, height=HEIGHT)
    canvas.grid()

    # (loc X, locY, x, y)
    canvas.create_oval(10, 10, 100, 100, fill=blue, activefill=yellow)
    canvas.create_oval(100, 100, 200, 100)
    #canvas.create_oval()
    # STD stndard algoritme

    base.mainloop()

#print('### updating log.csv ###')
#os.system(updateCmd)

createUI()

# while True:
#         time.sleep(1)
#         print('### Update ###')
#         os.system(updateCmd)
#         with open('log.csv', 'r') as myCSVFile:
#                 reader = csv.reader(myCSVFile)
#                 for each in reader:
#                         remove = '                  '
#                         tempList.append(each[0][27:-2])
#                         checkConnection(each[0][27:-1])



print('### temp list ###')
print(tempList)
