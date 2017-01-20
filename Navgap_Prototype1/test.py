import sys
print(sys.version)
print()
print(sys.version_info)
print()
print(sys.api_version)

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
    ['a','b', dirF + dirL],
    ['b','a', dirL + dirF],
    ['b','c', dirF + dirL],
    ['c','b', dirF + dirR],
]

conDict = {
}

print()
startLoc = input('startLoc: ')
endLoc = input('endLoc: ')
print('------------')
print(locCon[0][2])
print('------------')
print()


hallo1 = 1
hallo2 = 3
print('hello world.')
print('{}{}'.format(hallo1, hallo2))
