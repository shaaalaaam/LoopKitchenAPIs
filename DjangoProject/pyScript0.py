import pandas as pd
import pymysql

# This function will return the timestamp in the required format before inserting it into the database
def timeStampHelper(tSB):
    ans=tSB[0:-4]
    return ans


# REAL WORK
# Read the CSV file
df = pd.read_csv('storeStatus.csv')
df1= pd.read_csv('menuHours.csv')
df2=pd.read_csv('timeZone.csv')


# reduce rows for testing purpose
df= df.iloc[:1000]
df1=df1.iloc[:1000]
df2= df2.iloc[:1000]
# if I can write a command to 
# print(df.head(5))
# Establish a connection to the MySQL database
conn = pymysql.connect(host='localhost', user='root', password='12345678', database='loopKitchenDB')

# Create a cursor object
cursor = conn.cursor()

# Loop through each row of the CSV file and insert the data into the MySQL table
for i,row in df.iterrows():
    cursor.execute("INSERT INTO store_status (store_id,status_,timestamp_utc) VALUES (%s, %s, %s)",
                   (row['store_id'], row['status_'], timeStampHelper(row['timestamp_utc'])))
    
for i,row in df1.iterrows():
    cursor.execute("INSERT INTO store_hours (store_id,day_of_week,start_time_local,end_time_local) VALUES (%s, %s, %s,%s)",
                   (row['store_id'], row['day_of_week'], row['start_time_local'],row['end_time_local']))
    
for i,row in df2.iterrows():
    cursor.execute("INSERT INTO store_timezone (store_id,timezone_str) VALUES (%s, %s)",
                   (row['store_id'], row['timezone_str']))

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
