def mergeSort(list1):
    if len(list1) > 1:
        mid = len(list1) // 2 
        left_list = list1[:mid]  # Corrected variable name here
        right_list = list1[mid:]  # Corrected variable name here
        
        # Recursive calls to sort both halves
        mergeSort(left_list)
        mergeSort(right_list)
        
        # Initial indexes for left, right, and main list
        i = 0
        j = 0 
        k = 0 
        
        # Merge the sorted halves
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i += 1
            else:
                list1[k] = right_list[j]
                j += 1
            k += 1
        
        # Copy any remaining elements of left_list, if any
        while i < len(left_list):
            list1[k] = left_list[i]
            i += 1
            k += 1
        
        # Copy any remaining elements of right_list, if any
        while j < len(right_list):
            list1[k] = right_list[j]
            j += 1
            k += 1

# Example usage
nums = [2, 4, 5, 1, 8, 6, 4, 11, 33, 4, 67, 4, 3, 2, 2, 12, 9090]
mergeSort(nums)
print(nums)
