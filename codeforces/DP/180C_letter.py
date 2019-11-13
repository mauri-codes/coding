import re
letter = input()
uppercaseGroup = r'[A-Z]+'
lowercaseGroup = r'[a-z]+'
firstUpperCase = False
lastUpperCase = False

if re.search(uppercaseGroup, letter[0]):
   firstUpperCase = True
if re.search(uppercaseGroup, letter[len(letter)-1]):
   lastUpperCase = True

lower = re.split(uppercaseGroup, letter)
upper = re.split(lowercaseGroup, letter)

if firstUpperCase:
   upper[0] = ''

lower = list(filter(lambda group: group != '', lower))
upper = list(filter(lambda group: group != '', upper))
lower = list(map(lambda group: len(group), lower))
upper = list(map(lambda group: len(group), upper))



acc = 0
for group in range(len(upper)-1, -1, -1):
   acc += upper[group]
   upper[group] = acc
acc = 0
for group in range(len(lower)):
   acc += lower[group]
   lower[group] = acc



minOperations = float("inf")

for group in range(len(upper)):
   leftSum  = upper[group] + (lower[group-1] if (group != 0) else 0)
   rightSum = lower[group] + (upper[group+1] if (group+1 != len(upper)) else 0)
   minOperations = min(leftSum, rightSum, minOperations)

print(minOperations if minOperations != float("inf") else 0)

