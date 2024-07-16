
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    maxRep = 2
    
    k = 0
    visitedValues = []
    
    for i in range(len(nums)):
        if nums[i] not in visitedValues:
            visitedValues.append(nums[i])
            nums[k] = nums[i]
            k += 1
        elif(visitedValues.count(nums[i]) < maxRep):
            visitedValues.append(nums[i])
            nums[k] = nums[i]
            k += 1
        else:
            continue
    return k

nums = [0,0,1,1,1,1,2,3,3]
k = removeDuplicates(nums)
print(k, nums[:k])