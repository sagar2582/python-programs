def rotateArray(arr, n, d):
    temp = []
    i = 0
    while(i<d):
        temp.append(arr[i])
        i+=1
    i = 0
    while(d<n):
        arr[i] = arr[d]
        i+=1
        d+=1
    arr[:] = arr[: i] + temp
    return arr

arr = [1,2,3,4,5,6,7]
print(rotateArray(arr, len(arr), 2))