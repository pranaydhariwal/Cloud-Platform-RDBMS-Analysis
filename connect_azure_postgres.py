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
    conn = psycopg2.connect(database = "postgres", user = "user@postgre678", password = "Trial@123", host = "postgre678.postgres.database.azure.com", port = "5432")
    conn.close()
    stop = timeit.default_timer()
    t.append_row([i+1 ,stop - start])
    times.append(stop-start)

print(times)
std = np.std(times)
print([np.mean(times) + (1.725 * std/math.sqrt(20)), np.mean(times) - (1.725 * std/math.sqrt(20))])

'''
0.50108688965 && 0.019851789527501457
[0.5209386791775015, 0.4812351001224986]
[0.602643226, 0.5124537080000001, 0.5065570800000001, 0.518401468, 0.507686911, 0.5135022550000001, 0.5114814559999998, 0.510950615, 0.46644516000000014, 0.4557467559999999, 0.4094932380000005, 0.5120007229999999, 0.5107470110000003, 0.41230379600000067, 0.509989021, 0.5128452339999994, 0.5141373550000008, 0.40827575900000035, 0.51115976, 0.6149172610000004]
'''

'''cur.execute("SELECT * from townstest")
rows = cur.fetchall()
for row in rows:
    print(rows[0])
conn.close()'''
