def linearsearch(arr,key):
    for element in arr:
        if element == key:
            return True
    return False

arr = [1,2,3,4,5,6]
print(linearsearch(arr,3))
print(linearsearch(arr,9))
