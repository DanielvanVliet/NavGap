predecessors = {'RPI_AP2': None, 'RPI_AP3': 'RPI_AP2', 'RPI_AP1': 'RPI_AP2'}
for each in predecessors:
    if predecessors.get(each) != None:
        print('create line between {} and {}'.format(each, predecessors.get(each)))
