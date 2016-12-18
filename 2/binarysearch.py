def binarysearch(arr, key):
    head = 0
    tail = len(arr)-1
    while(head <= tail):
        mid = (head + tail) // 2
        if arr[mid] == key:
            return True
        else:
            if key < arr[mid]:
                tail = mid-1
            else:
                head = mid+1
    return False

arr = [1,2,3,4,5,6,7,8]
print(binarysearch(arr,4))
print(binarysearch(arr,10))
