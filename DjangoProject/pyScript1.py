import pymysql

# Establish a connection to the database
conn = pymysql.connect(host='localhost', user='root',
                       password='12345678', database='loopKitchenDB')


# Define a cursor object to interact with the database
cursor = conn.cursor()

# Write a SQL query to retrieve the business hours data
query = "SELECT * FROM store_status"

# Execute the query
cursor.execute(query)

# Retrieve the results and print them out
results = cursor.fetchall()
for row in results:
    print(row)

# Close the cursor and the database connection
cursor.close()
conn.close()
