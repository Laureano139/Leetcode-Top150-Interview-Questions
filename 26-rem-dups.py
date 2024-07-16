def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    k = 0
    visitedValues = []
    
    for i in range(len(nums)):
        if nums[i] not in visitedValues:
            visitedValues.append(nums[i])
            nums[k] = nums[i]
            k += 1
        else:
            continue
    return k

nums = [1, 1, 2]
k = removeDuplicates(nums)
print(k, nums[:k])