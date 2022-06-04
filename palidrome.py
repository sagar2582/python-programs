def isPalindrome(str):
    for i in range(0, int(len(str)/2)):
        n = len(str)
        if str[i] != str[n-i-1]:
            return False
    return True

# main function
s = "malayalam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")