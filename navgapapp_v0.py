### Navgap App ver. 0
## Simple navigation between 3 points, hardcoded.
# Written by Michel Baartman & Daniel van Vliet

import sys
print(sys.version)
print()
print(sys.version_info)
print()
print(sys.api_version)

## defines description for route
dirL = 'links '
dirR = 'rechts '
dirF = 'vooruit '
dirB = 'achteruit '

locList = [
    'a',
    'b',
    'c'
]

locCon = [
    ['a','b',1, dirF, dirL],
    ['b','a',1, dirL, dirF],
    ['b','c',2, dirF, dirL],
    ['c','b',2, dirF, dirR],
]

conDict = {
}

## list for pathing between points.
locConP1 = [
    ['a', 'b', dirF, dirL, dirF],
    ['a', 'c', dirF, dirL, dirF, dirR, dirF, dirL, dirF],
    ['b', 'c', dirF, dirL, dirF]
]

## function to determine path
def prototype1(startLoc, endLoc):
    routeList = []
    for each in locConP1: ## checks each line in list locConP1
        if each[0] == startLoc and each[1] == endLoc: ## if it finds the right pre-determined route, it adds the route to routeList
            counter = 2
            while counter < len(each):
                routeList.append(each[counter])
                counter += 1

        if each[1] == startLoc and each[0] == endLoc: ## if it can't find the path, it then turns the checks around
            counter = len(each)                       ## if it finds the reversed checks, then adds the directions to routeList
            while counter > 2:                        ## in a reversed manner.
                if each[counter-1] == dirR: ## swaps dirR with dirL
                    routeList.append(dirL)
                elif each[counter-1] == dirL: ## swaps dirL with dirR
                    routeList.append(dirR)
                else:
                    routeList.append(each[counter-1])
                counter -= 1

    for each in routeList:
        print(str(each)) ## prints routeList

## basic algorithm test, WIP
# def knitRoute(startLoc, endLoc):
#     routeList = []
#     fastDist = 0
#
#     routeList2 = []
#     currentLoc = []
#     curDist = 0
#
#
#     # routebes knit algo ##
#     for each in locCon:
#         if each[0] == startLoc:
#             currentLoc.append(startLoc)
#             currentLoc.append(each[1])
#             curDist += each[2]
#             print('{} > {}, Distance: {}'.format(currentLoc[0], currentLoc[1], curDist))
#
#         if each[1] == endLoc:
#             counter = 3
#             while counter < len(each):
#                 routeList2.append(each[counter])
#                 counter += 1
#
#             if curDist < fastDist:
#                 fastDist = curDist
#
#     print(routeList2)
#
#
#
#     # for each in locCon:
#     #     if each[0] == startLoc:
#     #         counter = 2
#     #         while counter < len(each):
#     #             routeList.append(each[counter])
#     #             counter += 1
#     # print(routeList)

while True: ## start of the application loop
    print()
    print('-startapp-')
    print('------------')
    startLoc = input('startLoc: ')
    if startLoc == 'end': ## you can break the app by entering "end" as start loc
        print('ending app')
        break
    endLoc = input('endLoc: ')
    prototype1(startLoc, endLoc) ## runs the algorithm script
    # update() ## in the future, update will probably be located somewhere in this list

    #knitRoute(startLoc, endLoc)
    #print(locCon[0][2])
    print('------------')
    print('-endapp-')

print()
hallo1 = 1
hallo2 = 3
print('hello world.')
print('{}{}'.format(hallo1, hallo2))
