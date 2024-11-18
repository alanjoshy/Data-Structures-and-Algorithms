def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        left= [] 
        right = []
        middle = []
        pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
        for x in arr:
            if x < pivot:
                left.append(x)
            elif x > pivot:
                right.append(x)
            else:
                middle.append(x)
        return quicksort(left) + middle + quicksort(right)

# Example usage
nums = [1, 252, 5, 145, 1241, 345, 134, 141, 5, 346, 3425, 2436]
sorted_nums = quicksort(nums)
print(sorted_nums)

















