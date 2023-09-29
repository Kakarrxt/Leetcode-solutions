def isMonotonic(nums):
    ins = dec = True
    if (len(nums) < 2):
        return True
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            dec = False
        elif nums[i] < nums[i - 1]:
            ins = False
    return ins or dec        




elements = list(map(int, input().split()))
print(isMonotonic(elements))                