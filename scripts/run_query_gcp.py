import mysql.connector
import timeit
import numpy as np
import math
from beautifultable import BeautifulTable
from mysql.connector import errorcode

config = {
  'host':'104.154.187.202',
  'user':'root',
  'password':'',
  'database':'trial'
}

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
      query =  "SELECT * FROM posts;"
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
