def bubbleSort(nums):
    for i in range(len(nums) - 1 , 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]: 
                nums[j],nums[j+1] = nums[j+1] ,nums[j]
                
nums = [3,4,32,34,263,423,23,56,1,19,41] 
bubbleSort(nums) 
print(nums)  




