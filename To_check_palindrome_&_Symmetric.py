def isPalindrome(str):
    for i in range(0, int(len(str)/2)):
        n = len(str)
        if str[i] != str[n-i-1]:
            print("It's not a palindrome")
    print("Yes, It's a palindrome")


def isSymmetric(str):
    n = len(str)
    
    if n%2 == 0:
        mid = n//2+1
    else:
        mid = n//2
        
    start1 = 0
    start2 = mid
    counter = 1
    while(start1 < mid and start2 < n):
        if str[start1] == str[start2]:
            start1 += 1
            start2 += 2
        else:
            counter = 1
            break
    
    if counter==0:
        print("Yes, It's Symmetric")
    else:
        print("It's not Symmetric")

    
    
# main function
s = "racecar"
isPalindrome(s)
isSymmetric(s)
 
