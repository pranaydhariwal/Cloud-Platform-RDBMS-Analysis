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
1.08064810095 && 0.20520314644934745
[0.785688868, 0.7644703749999999, 0.8292196289999998, 0.8678427219999998, 0.9342763540000005, 0.8824780680000002, 0.8791161219999992, 0.8551823259999995, 0.7956862170000001, 0.8719275530000008, 0.9137565149999993, 0.8459595550000003, 0.7989302880000011, 0.7996355919999978, 0.8483488819999998, 0.8062268010000011, 2.89387756, 1.8449647329999976, 1.902699965, 1.4926738939999993]
[1.2858512473993473, 0.8754449545006525]
'''

'''
3.8806530340000003 && 0.04131935281871752
[4.0586085789999995, 3.8049547539999997, 3.848091103, 3.840074038999999, 3.8801794019999996, 3.9490437850000006, 3.8512063070000018, 4.025034474999998, 3.779419134000001, 3.788680307, 3.8341791210000054, 3.9489728730000024, 3.845443500000002, 4.170614684, 3.807358812000004, 3.8893135389999998, 3.788991527999997, 3.971071073999994, 3.809499097, 3.722324567000001]
[3.9219723868187177, 3.839333681181283]
'''
