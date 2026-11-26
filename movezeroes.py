nums = [0,1,0,3,0,2]
j = 0
c = 0
for i in range(0,len(nums)):
    if nums[i] != 0:
        nums[j] = nums[i]
        j += 1
for i in range(j,len(nums)):
    nums[i] = 0
print(nums)
