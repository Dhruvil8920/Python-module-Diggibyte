from collections import Counter
list_=[]
N =int(input())
for i in range(N):
    list_ += [input()]
list_ = Counter(list_).items()
print(len(list_))
for key , value in list_ :
    print(value , end=' ')
