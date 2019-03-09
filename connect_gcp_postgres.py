#!/usr/bin/python

import psycopg2
import timeit
import numpy as np
import math
import matplotlib.pyplot as plt
from beautifultable import BeautifulTable


t = BeautifulTable()
x = list()
y = list()
t.column_headers = ["Connection #", "time"]
times = []

for i in range(0,20):
    start = timeit.default_timer()
    conn = psycopg2.connect(database = "postgres", user = "postgres", password = "Trial@123", host = "35.222.197.114", port = "5432")
    conn.close()
    stop = timeit.default_timer()
    t.append_row([i+1 ,stop - start])
    x.append(i+1)
    y.append(stop-start)
    times.append(stop-start)
plt.plot(np.array(x),np.array(y), color='C1')
plt.xticks(np.arange(min(x)-1, max(x), 2.0))
plt.xlabel("Iteration")
plt.ylabel("Time(ms)")
plt.legend(['GCP'])
plt.show()

print(y)
#print(t)
std = np.std(times)
print([np.mean(times) + (1.725 * std/math.sqrt(20)), np.mean(times) - (1.725 * std/math.sqrt(20))])

'''
0.28417115139999993 && 0.007083877945598465
[0.2912550293455984, 0.2770872734544015]
[0.28645943399999996, 0.276781123, 0.27733093100000006, 0.27844708900000004, 0.27814426700000006, 0.273114493, 0.2755333790000003, 0.27902916499999986, 0.2808963929999999, 0.35871447000000023, 0.2774887939999999, 0.2773860370000003, 0.2815595099999997, 0.2748836609999996, 0.27906320999999945, 0.2767926559999996, 0.28709123899999955, 0.3053111709999996, 0.28281622600000045, 0.2765797800000005]
'''

'''

'''

'''cur.execute("SELECT * from townstest")
rows = cur.fetchall()
for row in rows:
    print(rows[0])
conn.close()'''
