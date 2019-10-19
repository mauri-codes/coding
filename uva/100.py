
from sys import stdin, stdout


def operation (num):
  if num == 1:
    return 1
  if num % 2 == 0:
    return operation(num / 2) + 1
  else:
    return operation(3*num + 1) + 1

for line in stdin:
  a, b = line.split(' ')
  a = int(a)
  b = int(b)
  maxResult = 0
  for i in list(range(min(a, b), max(a, b))):
    maxResult = max(maxResult, operation(i))

  print(a,b,maxResult)

