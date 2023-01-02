import numpy

row , col = map(int,input().split())
lis=[]
for i in range(row):
    lis.append(list(map(int,input().split())))
a = numpy.array(lis)
print(numpy.max(numpy.min(a, axis=1)))