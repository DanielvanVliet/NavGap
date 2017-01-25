import csv
import os
import time

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

