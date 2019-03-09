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

'''
1.2372984433999998 && 0.056937657071872726
[0.850448358, 1.133643761, 1.0445694760000004, 1.0063678600000001, 1.1635510899999995, 1.2912969349999992, 1.1766753469999998, 1.3074984, 1.200369964, 1.304622825000001, 1.262276903, 1.4070401429999997, 1.5111925699999986, 1.2558002290000019, 1.293495857, 1.362120705999999, 1.2833682059999987, 1.3390997529999993, 1.3835291579999982, 1.1690013270000037]
[1.2942361004718725, 1.1803607863281271]
'''

'''
5.6773454016 && 1.3107586758899277
[7.387361831000001, 4.1057277469999995, 8.370545516, 3.887410366000001, 3.8132997759999974, 4.582595660000003, 4.009711883000001, 3.810223784999998, 4.4156053580000005, 4.267010856999995, 3.943838593999999, 17.976829971, 10.995921945000006, 4.570124716999999, 4.293290284999998, 3.818357852999995, 3.7576130500000033, 4.267348663000007, 7.330943376999997, 3.943146798000001]
[6.988104077489928, 4.366586725710072]
'''
