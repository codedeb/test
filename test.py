def exchangeZero(nums):
    i = 0
    j = 0
    while i < len(nums):
        if nums[i] != 0:
            nums[j], nums[i]= nums[i], nums[j]
            j += 1

        i += 1
    return nums


obj = exchangeZero([1,0,1,0,1,1,0,1])

print(obj)
