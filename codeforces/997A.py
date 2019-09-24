A, B, C, N = map(int, input().split())
not_passed = N - (A + B - C)
if A + B - C < N and A >= C and B >= C:
  print (not_passed)
else:
  print (-1)
