''' Countbits
return number of 1's in binary representation of int
5 -> 101 -> 2 (2 is the output)
7 -> 111 -> 3'''

def bruteforce(n):                  # T.C = O(n)
  s = str(bin(n))[2:]
  print("{}".format(s))
  return s.count('1')

def cntbits(n):
  c=0
  while n:
    c+=1
    n = n & (n-1)
  return c 

n = int(input())
print(bruteforce(n))
print(cntbits(n))