import numpy as np

n = int(input())

a = np.array([list(map(float, input().split())) for i in range(n)])

print(np.round(np.linalg.det(a), 2))