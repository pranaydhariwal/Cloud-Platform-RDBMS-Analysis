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

'''
0.20746566894999993 && 0.006896023511228128
[0.23299667899999998, 0.20398862299999998, 0.20219450900000002, 0.19883350199999994, 0.201280613, 0.20211438400000015, 0.19808827499999992, 0.19933045900000002, 0.20419110699999998, 0.20606690799999994, 0.19798969499999997, 0.209372444, 0.20089930000000011, 0.20078726800000002, 0.20651541500000015, 0.200678248, 0.20678688199999984, 0.199474881, 0.2784146629999995, 0.19930952399999935]
[0.21436169246122805, 0.20056964543877182]
'''
