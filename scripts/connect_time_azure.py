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
  'database':'trial',
}

t = BeautifulTable()
t.column_headers = ["Connection #", "time"]

times = []

# Construct connection string
for i in range(0,20):
  try:
     start = timeit.default_timer()
     conn = mysql.connector.connect(**config)
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    cursor = conn.cursor()

    cursor.close()
    conn.close()
    stop = timeit.default_timer()
    t.append_row([i+1, stop - start])
    times.append(stop - start)
    i = i + 1

print(times)
std = np.std(times)
print([np.mean(times) + (1.725 * std/math.sqrt(20)), np.mean(times) - (1.725 * std/math.sqrt(20))])
