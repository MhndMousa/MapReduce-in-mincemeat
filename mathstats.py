import mincemeat
import sys
from math import sqrt


if len(sys.argv) < 2:
  print "Give me a file on the command-line"
  sys.exit(1)

file = open(sys.argv[1],'r')
data = list(file)
file.close()

print data[:10]



datasource=dict(enumerate(data) )

def mapfn(k,v):

    yield 'count', 1
    yield 'sum',float(v)
    yield 'deveiation', float (v) * float(v)







def reducefn(k,vs):
    result = sum(vs)
    return result

s=mincemeat.Server()
s.datasource=datasource
s.mapfn=mapfn
s.reducefn=reducefn
results = s.run_server(password="changeme")
stdev = sqrt((results['deveiation']/results['count']) - (results['sum']/results['count'])**2)
print ("std.dev: ",stdev)
print ("sum: ",(results['sum']))
print ("count: ",(results['count']))
