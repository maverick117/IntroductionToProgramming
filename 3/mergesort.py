def mergesort(A):
  if len(A) <= 1:
    return A
  L,R = mergesort(A[0:len(A)//2]) , mergesort(A[len(A)//2:len(A)])
  ret = []
  left, right = 0,0
  while left < len(L) and right < len(R):
    if L[left] <= R[right]:
      ret.append(L[left])
      left+=1
    else:
      ret.append(R[right])
      right+=1
  if left >= len(L):
    while right<len(R):
      ret.append(R[right])
      right += 1
  else:
    while left<len(L):
      ret.append(L[left])
      left += 1
  return ret

A = [5,3,6,4,3,8,9,7,6,1,2,5,10,0,34,23]
print(mergesort(A))
