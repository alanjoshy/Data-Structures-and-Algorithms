def selectionsort(nums):
    for i in range(len(nums)):
        minpos = i 
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j  # Update minpos instead of min
    
        nums[i], nums[minpos] = nums[minpos], nums[i]  # Swap the values
    

nums = [1,252,5,145,1241,345,134,141,5,346,3425,2436] 
selectionsort(nums) 
print(nums)