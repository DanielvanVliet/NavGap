import pymysql.cursors

connection = pymysql.connect(host='localhost',
			     user='root',
			     password='navgap',
			     db='navgapdb',
			     charset='utf8mb4')


curs = connection.cursor()

def add_lines(location1, location2, distance):
	location1 = "'" + location1 + "'"
	location2 = "'" + location2 + "'"
	query = "INSERT INTO LocationConnections values("+location1+', '+location2+", "+distance+")"
	print("Query = "+query)
	curs.execute(query)
	connection.commit()
	print("next connection between location")
	print()

def add_lines2(location, description, ssid):
	location = "'" + location + "'"
	description = "'" + description + "'"
	ssid = "'" + ssid + "'"
	print(ssid)
	query = "INSERT INTO Locations values("+location+', '+description+", "+ssid+")"
	print("Query = "+query)
	curs.execute(query)
	connection.commit()
	print("next locaton")

def drop_table(name):
	query = "DROP TABLE "+name
	print("Query = "+query)
	curs.execute(query)
	connection.commit()

def create_locationConnections():
	query = "CREATE TABLE LocationConnections(Location1 varchar(1), Location2 varchar(1), Afstand NUMERIC)"
	print("Query = "+query)
	curs.execute(query)
	connection.commit()
	print("Table LocationConnections created")

def create_locations():
	query = "CREATE TABLE Locations(Location varchar(1), Description text, SSID text)"
	print("Query = "+query)
	curs.execute(query)
	connection.commit()
	print("Table Locations created")

def add_locationConnections(number):
	counter = 0
	while counter != number:
		L1 = input("Location1?")
		L2 = input("Location2?")
		D = input("Afstand tussen Location1 en Location2?")
		counter += 1
		add_lines(L1, L2, D)

def add_location(number):
	counter = 0
	while counter != number:
		L = input("Location? ")
		d = input("Descripion of this location? (for example A - Aap): ")
		W = input("Wifi-SSID for this location? ")
		counter += 1
		add_lines2(L, d, W)

def displaytable(table):
	query = "SELECT * FROM "+str(table)
	print("Query = "+query)
	curs.execute(query)
	connection.commit()
	print()
	for row in curs.fetchall():
		 print(str(row[0])+" 	"+str(row[1])+" 	"+
		 str(row[2]))		
	print()

while True:
	print("Option 1: create table Locations")
	print("Option 2: create table LocationConnections")
	print("Option 3: add location to Locations")
	print("Option 4: add connection between Locations")
	print("Option 5: drop a table")
	print("Option 6: display a table")
	print("Option 7: quit program")
	option = int(input("Choose option by entering a number 1-7: "))
	print()
	if option == int(1):
		create_locations()
	elif option == int(2):
		create_locationConnections()
	elif option == int(3):
		temp = int(input("How many locations? "))
		add_location(temp)
	elif option == int(4):
		temp = int(input("How many connections between locations? "))
		add_locationConnections(temp)
	elif option == int(5):
		tablename = input("Which table do you want to drop? ")
		drop_table(tablename)
	elif option == int(6):
		temp = input("Which table do you want to print? ")
		displaytable(temp)
	else:
		break
