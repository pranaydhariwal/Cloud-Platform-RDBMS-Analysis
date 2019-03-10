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
