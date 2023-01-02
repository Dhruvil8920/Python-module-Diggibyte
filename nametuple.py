from collections import namedtuple
total = int(input())
Student = namedtuple('Student', input())

sum = 0
for _ in range(total):
    y = Student(*input().split())
    sum += int(y.MARKS)
print(sum/total)