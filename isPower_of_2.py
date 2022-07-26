'''
Is power of 2
n ->  Input
True/Flase  -> output
check if its a sqaure of 2 or not
'''
def check_powerof2(n):         # T.C -> O(1)
  x = n
  y = not(n & (n-1))
  return x and y


n = int(input())
print(check_powerof2(n))