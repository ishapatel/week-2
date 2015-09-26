
import pyorient
import sys

client = pyorient.OrientDB("localhost", 2424)
session_id = client.connect("root", "R0n+H3rm10n3")
db_name = "soufun2"
db_username = "root"
db_password = "R0n+H3rm10n3"

if client.db_exists( db_name, pyorient.STORAGE_TYPE_MEMORY ):
	client.db_open( db_name, db_username, db_password )
	print db_name + " opened successfully"
else:
	print "database [" + db_name + "] does not exist! session ending..."
	sys.exit()

lat1 = 22.532498
lat2 = 22.552317

lng1 = 114.044329
lng2 = 114.076644

query = 'SELECT FROM Listing WHERE latitude BETWEEN {} AND {} AND longitude BETWEEN {} AND {}'

records = client.command(query.format(lat1, lat2, lng1, lng2))

numListings = len(records)

print 'received ' + str(numListings) + ' records'

# [ANALYZE THE RETURNED RECORDS TO DETERMINE THE MINIMUM, MAXIMUM, AND AVERAGE PRICE OF THE LISTINGS]
# Hint: the loop that you need to look into each record is already provided below.
# To find the average price, add up all the prices and divide by the number of results
# To find the minimum price, create a variable and initialize it to a very large number, 
# then test each price to see if it is smaller than the current minimum. If it is, update 
# the minimum variable with that price. You can do something similar to find the maximum.

ini_min = 900  
ini_max = 0
sum_rec = 0

for record in records:
	print record.price
	sum_rec += record.price
	avg_price = sum_rec/len(records)
	if record.price < ini_min:
	    min_price = record.price
	    ini_min = min_price
	else:
	   min_price = ini_min
	if record.price > ini_max:
	    max_price = record.price
	    ini_max = max_price
	else:
	    max_price = ini_max   
	    	 
	       


# [PRINT OUT THE RESULTING VALUES BY CONCATENATING THEM TO THESE LINES TO CHECK YOUR WORK]

print 'min price: ' + str(min_price)
print 'max price: ' + str(max_price)
print 'average price: ' + str(avg_price)

client.db_close()
