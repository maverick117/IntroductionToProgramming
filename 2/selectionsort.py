def sort(arr):
    for j in range(len(arr)-1):
        minNum = j
        for i in range(j,len(arr)):
            if arr[minNum] > arr[i]:
                minNum = i
        if minNum != j:
            tmp = arr[minNum]
            arr[minNum] = arr[j]
            arr[j] = tmp
    return arr

a = [5,3,7,4,5,7,9,2]
a = sort(a)
print(a)
