n = int(input())
nums = []

for i in range(n):
  nums.append(int(input()))

for i in range(n):
  for j in range(1,n - i):
    if(nums[j-1] > nums[j]):
      tmp = nums[j-1]
      nums[j-1] = nums[j]
      nums[j] = tmp

for i in range(n):
  print(nums[i],end = ' ')
print()
