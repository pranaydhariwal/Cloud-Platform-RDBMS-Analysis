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
