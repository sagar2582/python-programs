def ajeeb(arr, n):
    result = 1
    for i in arr:
        result = result*i
    return (result % n)






# Driver 
arr=[100,10,5,25,35,14]
n = 11    
print(ajeeb(arr,n))