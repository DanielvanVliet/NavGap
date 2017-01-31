import pymysql.cursors

connection = pymysql.connect(host='localhost',
			     user='root',
			     password='navgap',
			     db='navgapdb')


curs = connection.cursor()

#Imports ssid from db into python dictionary
spotDict = {}
curs.execute("SELECT * FROM Locations")
connection.commit()

for row in curs.fetchall():
	spotDict[row[0]] = [False, 0, row[1], row[2]]
print(spotDict)
