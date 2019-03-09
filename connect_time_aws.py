import mysql.connector
import timeit
import numpy as np
import math
from beautifultable import BeautifulTable
from mysql.connector import errorcode

config = {
  'host':'dbinstance.c6zmxwufoiot.us-east-2.rds.amazonaws.com',
  'user':'pranaydhariwal',
  'password':'pwaosrsd',
  'database':'test'
}

t = BeautifulTable()
t.column_headers = ["Connection #", "time"]
times = []

# Construct connection string
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
0.3143785212 && 0.0014096368394640535
[0.31578815803946403, 0.31296888436053594]
[0.325898597, 0.314583067, 0.31668127300000004, 0.3146646580000001, 0.31194813600000004, 0.31051776399999986, 0.3105517899999999, 0.3119040179999999, 0.31673643500000015, 0.3140016750000001, 0.3163027930000002, 0.31005882699999976, 0.3179121429999996, 0.30901401800000006, 0.3131804970000003, 0.31334894300000027, 0.31706729099999986, 0.31607357599999997, 0.3150007530000005, 0.3121241699999997]
'''
