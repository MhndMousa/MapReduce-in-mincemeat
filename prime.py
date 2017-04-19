#!/usr/bin/env python
import mincemeat
import sys

data = [""] * 10000
for i in range(10000):
    data[i % len(data)] += str(i * 1000)
for i in range(len(data)):
    data[i] = int(data[i])+1

# The data source can be any dictionary-like object
datasource = dict(enumerate(data))

def mapfn(k, v):
    for i in range(v, v+1000):
        if len(str(i)) % 2 == 0:
            pass
        elif not(str(i) == str(i)[::-1]):
            pass
        else:
            prime = True;
            for a in range(3 ,i/2, 2):
                if i % a == 0:
                    pass
                    prime = False

            if prime:
                yield "Numbers", i
                yield "sum", i
                yield "count", 1
                prime = True

def reducefn(k, vs):
    return vs

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print ("Numbers:", results["Numbers"])
print ("sum: ", sum(results["sum"]))
print ("Count: ", sum(results["count"]))
