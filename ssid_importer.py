import pymysql.cursors

connection = pymysql.connect(host='localhost',
			     user='root',
			     password='navgap',
			     db='navgapdb')


curs = connection.cursor()

#Imports ssid from db into python dictionary
ssid_dict = {}
curs.execute("SELECT * FROM Locations")
connection.commit()

for row in curs.fetchall():
	ssid_dict[row[0]] = row[2]
print(ssid_dict)

