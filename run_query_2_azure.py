import mysql.connector
import timeit
import numpy as np
import math
from beautifultable import BeautifulTable
from mysql.connector import errorcode

# Obtain connection string information from the portal
config = {
  'host':'mysql-server678.mysql.database.azure.com',
  'user':'user@mysql-server678',
  'password':'Trial@123',
  'database':'trial'
}

# Construct connection string
t = BeautifulTable()
t.column_headers = ["Connection #", "Query" ,"time"]
times = []

for i in range(0,20):
    try:
       conn = mysql.connector.connect(**config)
       #print("Connection established")
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
    else:
      cursor = conn.cursor()

      start = timeit.default_timer()
      query =  "SELECT * FROM authors where id IN (SELECT author_id from posts);"
      cursor.execute(query)
      rows = cursor.fetchall()
      cursor.close()
      conn.close()
      stop = timeit.default_timer()
      t.append_row([i+1, query ,stop - start])
      times.append(stop-start)

print(times)
std = np.std(times)
print([np.mean(times) + (1.725 * std/math.sqrt(20)), np.mean(times) - (1.725 * std/math.sqrt(20))])

'''
0.78948541025 && 0.0415682416495479
[0.905145146, 0.846894678, 1.002578326, 0.7334152240000007, 1.0952537910000002, 0.9060822159999997, 0.7330705710000007, 0.7123590330000003, 0.828121874999999, 0.8014067049999998, 0.7434562539999998, 0.7336595679999984, 0.7444096640000009, 0.7524821729999989, 0.7362028550000019, 0.7017159820000032, 0.7000509619999988, 0.7004299950000004, 0.6940354739999997, 0.718937712999999]
[0.8310536518995478, 0.7479171686004521]
'''

'''
3.8156119699000017 && 0.08250828070132672
[3.70305994, 3.9698803720000004, 3.6879432100000002, 3.6751299590000013, 3.6651771020000012, 3.676868005000003, 3.6216464360000025, 3.6552003240000026, 3.6689011210000047, 3.684090762000004, 3.7000634370000043, 3.6232778890000006, 4.028963996000002, 3.7259836520000036, 3.7922603740000014, 4.056447166999995, 3.7354381509999968, 4.217361564000001, 4.048557060000007, 4.3759888769999975]
[3.8981202506013286, 3.733103689198675]
'''
