import mincemeat
import sys
import hashlib


if len(sys.argv) < 2:
  print "Give me a hash to find"
  sys.exit(1)

data = ["abcdefghijklmnopqrstuvwxyz1234567890%s" % sys.argv[1]]

datasource= dict(enumerate(data) )

def mapfn(k,v):

    for first in range(len(v)-5):
        wordComb = str(v[first])
        word_hashed = hashlib.md5(str(v[first])).hexdigest()
        if str(word_hashed)[:5] == str(v)[-5:]:
            yield "found:", wordComb

        for second in range(len(v)-5):
            wordComb = str(v[first])+str(v[second])
            word_hashed = hashlib.md5(str(v[first])+str(v[second])).hexdigest()
            if str(word_hashed)[:5] == str(v)[-5:]:
                yield "found:", wordComb

            for third in range(len(v)-5):
                wordComb = str(v[first])+str(v[second])+str(v[third])
                word_hashed = hashlib.md5(str(v[first])+str(v[second])+str(v[third])).hexdigest()
                if str(word_hashed)[:5] == str(v)[-5:]:
                    yield "found:", wordComb

                for fourth in range(len(v)-5):
                    wordComb = str(v[first])+str(v[second])+str(v[third])+str(v[fourth])
                    word_hashed = hashlib.md5(str(v[first])+str(v[second])+str(v[third])+str(v[fourth])).hexdigest()
                    if str(word_hashed)[:5] == str(v)[-5:]:
                        yield "found:", wordComb


def reducefn(k,vs):
    return vs

s=mincemeat.Server()
s.datasource=datasource
s.mapfn=mapfn
s.reducefn=reducefn
results = s.run_server(password="changeme")

print results
