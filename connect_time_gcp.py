import mysql.connector
import timeit
import numpy as np
import math
from beautifultable import BeautifulTable
from mysql.connector import errorcode

# Obtain connection string information from the portal
config = {
  'host':'104.154.187.202',
  'user':'root',
  'password':'',
  'database':'trial'
}

t = BeautifulTable()
t.column_headers = ["Connection #", "time"]
times = []

for i in range(0,20):
  try:
     start = timeit.default_timer()
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

    cursor.close()
    conn.close()
    stop = timeit.default_timer()
    t.append_row([i+1, stop - start])
    times.append(stop-start)
    i = i + 1

print(times)
std = np.std(times)
print([np.mean(times) + (1.725 * std/math.sqrt(20)), np.mean(times) - (1.725 * std/math.sqrt(20))])
'''
0.18785919585000002 && 0.007805526266230972
[0.275545568, 0.18182175000000006, 0.18539019300000004, 0.18169653400000008, 0.18795197600000002, 0.18314614500000004, 0.18173413000000016, 0.18386064999999996, 0.18094817399999985, 0.1826072540000001, 0.18315982400000008, 0.18714770199999986, 0.18119475299999976, 0.18369807000000016, 0.18277378000000022, 0.18614558199999998, 0.17991906899999988, 0.18051292499999994, 0.18609615499999999, 0.18183368300000025]
[0.19566472211623098, 0.18005366958376906]
'''
