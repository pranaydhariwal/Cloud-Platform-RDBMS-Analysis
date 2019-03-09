#!/usr/bin/python

import psycopg2
import timeit
import numpy as np
import math
from beautifultable import BeautifulTable


t = BeautifulTable()
t.column_headers = ["Connection #", "Query" ,"time"]
times = []
query = "SELECT * from townstest"

conn = psycopg2.connect(database = "postgres", user = "pranay", password = "pwaosrsd", host = "postgresql-mydbinstance.c6zmxwufoiot.us-east-2.rds.amazonaws.com", port = "5432")
cur = conn.cursor()

for i in range(0,20):
    start = timeit.default_timer()
    cur.execute(query)
    print("here")
    stop = timeit.default_timer()
    t.append_row([i+1, query ,stop - start])
    times.append(stop-start)

print(times)
std = np.std(times)
print([np.mean(times) + (1.725 * std/math.sqrt(20)), np.mean(times) - (1.725 * std/math.sqrt(20))])


'''
20.430687105200004 && 0.7548324194428423
[19.512570139, 18.692974479, 20.718801631000005, 22.178293339999996, 20.689848468000008, 21.960910999999996, 21.370296077999996, 20.191363410000008, 17.95882862800002, 18.034679648999997, 18.244025714000003, 20.080914129000007, 19.626471976999966, 19.588080976000015, 19.686861031999968, 27.02262405800002, 22.411285238000005, 20.37824642000004, 20.027233195999997, 20.23943254200003]
[21.185519524642846, 19.675854685757162]
'''
