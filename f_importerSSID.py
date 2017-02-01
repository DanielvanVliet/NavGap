import pymysql.cursors

def import_SSID():
	connection = pymysql.connect(host='192.168.0.2',
					 user='monitor',
					 password='navgap',
					 db='navgapdb',
					 charset='utf8mb4')


	curs = connection.cursor()

	#Imports ssid from db into python dictionary
	spotDict = {}
	curs.execute("SELECT * FROM Locations")
	connection.commit()

	for row in curs.fetchall():
		spotDict[row[0]] = [False, 0, row[1], row[2]]
	return spotDict
