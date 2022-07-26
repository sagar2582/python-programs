# Find all prime number till N

def gen_prime(n):
  prime = [True]*(n+1)
  prime[0] = False
  prime[1] = False
  for p in range(2, int(n**0.5)+1):
    if prime[p] == True:
      for i in range(p*p, n+1, p):
        prime[i] = False

  for i in range(0, len(prime)):
    if prime[i] == True:
      print(i, end =' ')


n = int(input())
gen_prime(n)