import csv
import os
import time

conList = [
	'MarcKYS',
	'essidhere',
        'Connectify-me'
]
tempList = []
connection = False
updateCmd = 'sudo /home/pi/navgap/navgapboot.sh start'

def checkConnection(essid):
        global connection
        for each in conList:
                #print('checking if {} is {}'.format(essid, each))
                if essid == each:
                        connection = True
                        print('######## DICHTBIJ POINT {} #########'.format(essid))
                elif connection == False:
                        print('## No Connection ##')

#print('### updating log.csv ###')
#os.system(updateCmd)

while True:
        time.sleep(1)
        print('### Update ###')
        os.system(updateCmd)
        with open('log.csv', 'r') as myCSVFile:
                reader = csv.reader(myCSVFile)
                for each in reader:
                        remove = '                  '
                        tempList.append(each[0][27:-2])
                        checkConnection(each[0][27:-1])           



print('### temp list ###')
print(tempList)
