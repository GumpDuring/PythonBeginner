nums = [-4,-1,0,3,10]
n = len(nums)
left,right= 0,n-1
i = n-1
a = [0] * n
while left <= right:
    if abs(nums[left]) < abs(nums[right]):
        a[i] = int(nums[right])**2
        right -= 1
    else:
        a[i] = int(nums[left])**2
        left += 1
    i -= 1
print(a)
