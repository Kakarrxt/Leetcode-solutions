def sortArrayByParity(nums):
    even = []
    odd = []
    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even + odd



elements = list(map(int, input().split()))

print(sortArrayByParity(elements))




        