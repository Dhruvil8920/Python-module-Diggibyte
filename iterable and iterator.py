from itertools import combinations
N,c= int(input()), 0
lis = input().split()
K = int(input())
cos = list(combinations(lis,K))
for i in cos:
    if 'a' in i:
        c += 1
print(c / len(cos))
