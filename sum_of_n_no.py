# Sum of n numbers

def func1(n):
  s=0
  for i in range(n+1):
    s+=i
  return s

# OR

def func2(n):
  return n*(n+1) // 2

n = int(input())
print(func1(n))
print(func2(n))