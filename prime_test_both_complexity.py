# Find the Prime Number Test  O(n) vs O(root(n))

def func1(n):
  c =0 
  for i in range(2,n):
    if n%i == 0:
      c+=1
  return (c == 0)


def func2(n):
  c = 0
  for i in range(2,int(n**0.5)+1):
    if n%i == 0:
      c+=1
  return (c==0)

n = int(input())
print(func1(n))
print(func2(n))