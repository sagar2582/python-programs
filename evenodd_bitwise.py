# Check for even and odd using Bitwise Operator

def func(n):
  if n&1 == 1:
    return 'odd'
  else:
    return 'even'

n = int(input())
print(func(n))