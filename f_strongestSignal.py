import csv
spotDict = {
    'RPI_AP2' : [False, 0, 50, 150],
    'Connectify-me' : [False, 0, 180, 90],
    'RPI_AP1' : [False, 0, 50, 50],
    'RPI_AP3' : [False, 0, 50, 50]
}
signalDict = {}
global userList
userList = []
def updateList():
    global spotDict
    global userList
    print('# update list #')
    updateCmd = 'sudo iwlist wlan0 scan |grep -e Signal -e ESSID'

    trueCount = 0

    # this is for pc testing, rips info from old log
    counter = 0
    for spot in spotDict:
        #print(' | Connection: {:15}: {}, strength: {}'.format(spot, spotDict[spot][0], spotDict[spot][1]))
        with open('log.csv', 'r') as file:
            reader = csv.reader(file)
            row = 0
            for line in reader:
                row += 1
                essid = line[0][27:-1]
                signal = line[0][49:51]
                if row % 2 == 1:
                    rowdata = signal
                    #print(rowdata)
                if essid == spot and int(rowdata) <= 70: # range limiter
                    #print('{} set to true, breaking for-loop'.format(essid))
                    spotDict[spot][0] = True
                    spotDict[spot][1] = rowdata
                    if counter <= 2:
                        signalDict[essid] = int(rowdata)
                        counter = len(signalDict)
                    else:
                        lowestInt = 0
                        for each in signalDict:
                            if signalDict[each] > lowestInt:
                                global lowest
                                lowestInt = signalDict[each]
                                lowest = each
                        if int(rowdata) < int(signalDict.get(lowest)):
                            signalDict[essid] = int(rowdata)
                            signalDict.pop(lowest)
                    break
                else:
                    spotDict[spot][0] = False
                    #print('{} set to false'.format(essid))
    for each in signalDict:
        userList.append(each)
updateList()
print('SignalDict {}'.format(signalDict))
print(spotDict)
print(userList)
