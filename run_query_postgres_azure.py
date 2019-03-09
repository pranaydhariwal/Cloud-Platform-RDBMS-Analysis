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

conn = psycopg2.connect(database = "postgres", user = "user@postgre678", password = "Trial@123", host = "postgre678.postgres.database.azure.com", port = "5432")
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
18.05613874755 && 0.2002873812710228
[17.990809503, 17.71785216, 18.480998121000006, 18.379092830000005, 18.21528515, 17.596037009, 18.03658172, 17.936764376, 17.799974564999985, 17.658329933999994, 17.554058231, 17.567757056000005, 17.682623292000017, 17.858244807000005, 19.479178622999996, 17.991194129999997, 18.22403594399998, 18.00474578699999, 19.321320426, 17.62789128700001]
[18.256426128821023, 17.85585136627898]
'''
