arr = [1,2,4,10,23,3]
k = 2
left = 0
right = 0
cs = 0
ms = arr[0]
while right < len(arr):
    cs += arr[right]
    length = right - left + 1
    if length == k:
        if cs > ms:
            ms = cs
        cs -= arr[left]
        left += 1
    right += 1
print(ms)    