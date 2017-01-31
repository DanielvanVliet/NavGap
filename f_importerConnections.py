graph = {'A':{'B':1, 'C':2}, 'B': {'A':1, 'C':1}, 'C':{'A': 2, 'B': 1}}
connectDict = {}
for each in graph:
    connectDict[each] = []
    for neighbor in graph.get(each):
        connectDict[each].append(neighbor)
print(connectDict)
