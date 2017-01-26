import csv
import os
import time
import tkinter

spotList = {
    'Connectify-me' : [False, 0],
    'RPI_AP2' : [False, 0]
}


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
        print('{} in EssidList'.format(essid))
        if essid in spotList:
            print('{} in spotList'.format(essid))
            tempList[essid] = SignalList[counter]
        counter += 1

while True:
    text = input('{null | break}')
    if text == 'break':
        break

    updateList()
    print(tempList)
