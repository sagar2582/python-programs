def factorial(num):
    return 1 if (num==1 or num==0) else num*factorial(num-1);

# Driver code
num = 5;
print("The factorial of", num, "is",factorial(num))