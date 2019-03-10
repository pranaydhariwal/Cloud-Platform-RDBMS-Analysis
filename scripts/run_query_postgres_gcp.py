#!/usr/bin/python

import psycopg2
import timeit
import numpy as np
import math
from beautifultable import BeautifulTable


t = BeautifulTable()
t.column_headers = ["Connection #", "Query" ,"time"]
times = []
query = "SELECT * from towns"

conn = psycopg2.connect(database = "postgres", user = "postgres", password = "Trial@123", host = "35.222.197.114", port = "5432")
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
