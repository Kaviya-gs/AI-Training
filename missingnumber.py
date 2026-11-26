nums = [0,1,3,4]
n = len(nums)
range_sum = n*(n+1)//2
nums_sum = sum(nums)
print(range_sum - nums_sum)