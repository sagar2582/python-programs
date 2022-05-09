def prime(x, y):
    prime_num = []
    
    for i in range(x,y):
        if i==0 or i==1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i%j == 0:
                    break
            else:
                    prime_num.append(i)
    return prime_num


# Driver Code
st_range = 2
ed_range = 14

lst = prime(st_range, ed_range)
if len(lst) == 0:
    print("There are no Prime Numbers in this list")
else:
    print("The Prime Numbers in the list are: ", lst)