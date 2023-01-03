import numpy

n, m = input().split()
A = []
for _ in range(int(n)):
    A.append(list(map(int, input().split())))

print(numpy.mean(numpy.array(A), axis=1))
print(numpy.var(numpy.array(A), axis=0))
print(round(numpy.std(numpy.array(A), axis=None), 11))

