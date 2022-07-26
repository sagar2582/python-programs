# All divisor of a number with root(n) complexity

def func1(n):
  ls = []
  for i in range(1,n+1):            # T.C = O(n)
    if n%i == 0:
      ls.append(i)
  return ls

def func2(n):
  ls = set()
  for i in range(1, int(n**0.5)+1):           # T.C = O(root(n))
    if n%i == 0:
      ls.add(i)
      ls.add(n//i)
  return list(ls)

n = int(input())
print(func1(n))
print(func2(n))