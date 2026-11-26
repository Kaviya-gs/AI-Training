nums = [2,3,4,5,5,6,6,6,7]
j = 1
for i in range(1,len(nums)):
    if nums[i] != nums[i-1]:
        nums[j] = nums[i]
        j += 1
print(j)
print(nums[:j]) 