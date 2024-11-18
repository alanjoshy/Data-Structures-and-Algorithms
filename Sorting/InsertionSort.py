def insertionSort(nums):
    for i in range(1,len(nums)):
        current = nums[i] 
        pos = i 
        while current < nums[pos- 1] and pos > 0:
            nums[pos] = nums[pos - 1] 
            pos  = pos -1 
        nums[pos] = current 
        
nums = [2,43,5,23,14,55,6,7,88,7] 
insertionSort(nums) 
print(nums)  


