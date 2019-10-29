
n = input()
int_list = map(int, input().split())

count = 0
zeroes = 0
negatives = 0


for num in int_list:
    if (num == 0):
        zeroes += 1
    else:
        count += (abs(num) - 1)
    if (num < 0):
        negatives += 1

if (zeroes == 0 and negatives%2 != 0):
    count +=2
else:
    count += zeroes
print(count)
