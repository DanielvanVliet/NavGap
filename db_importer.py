import pymysql.cursors

connection = pymysql.connect(host='localhost',
			     user='root',
			     password='navgap',
			     db='navgapdb',
			     charset='utf8mb4')


curs = connection.cursor()

#Imports data from db into python dictionary
locations = []
curs.execute("SELECT * FROM Locations")
connection.commit()
for row in curs.fetchall():
	locations.append(row[0])

graph = {}


for each in locations:
	curs.execute("SELECT * FROM LocatieConnecties")
	connection.commit()
	graph[each] = {}
	temp = []
	for row in curs.fetchall():
		if row[0] == each:
			temp.append([str(row[1]), int(row[2])])
	for neighbor in temp:
		graph[each][neighbor[0]] = neighbor[1] 
print(graph)
