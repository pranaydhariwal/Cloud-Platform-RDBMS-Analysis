#!/usr/bin/python

import psycopg2
import timeit
import numpy as np
import math
from beautifultable import BeautifulTable


t = BeautifulTable()
t.column_headers = ["Connection #", "time"]
times = []

for i in range(0,20):
    start = timeit.default_timer()
    conn = psycopg2.connect(database = "postgres", user = "pranay", password = "pwaosrsd", host = "postgresql-mydbinstance.c6zmxwufoiot.us-east-2.rds.amazonaws.com", port = "5432")
    conn.close()
    stop = timeit.default_timer()
    t.append_row([i+1 ,stop - start])
    times.append(stop-start)

print(times)
std = np.std(times)
print([np.mean(times) + (1.725 * std/math.sqrt(20)), np.mean(times) - (1.725 * std/math.sqrt(20))])

'''
0.1529160314 && 0.0010313067304399254
[0.15394733813043993, 0.1518847246695601]
[0.15957013100000006, 0.15293150700000002, 0.14974636899999993, 0.15065913399999997, 0.15275742599999997, 0.155795366, 0.149550737, 0.15412106000000003, 0.15274708599999998, 0.15491209000000006, 0.1492673769999997, 0.15488500000000016, 0.15295544800000016, 0.15129938900000006, 0.15378806899999997, 0.15086195299999972, 0.15179038799999978, 0.15302001399999998, 0.14991223900000028, 0.1577498450000001]
'''
'''cur.execute("SELECT * from townstest")
rows = cur.fetchall()
for row in rows:
    print(rows[0])
conn.close()'''
