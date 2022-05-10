x = 11
if x > 1:
    
    for i in range(2, int(x**0.5)+1):
        if (x % i == 0):
            print("It's not a prime")
            break
    else:
        print("It's a prime")
else:
    print("It's not a prime")