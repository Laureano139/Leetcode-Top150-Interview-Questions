"""
You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. 
Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    
    alcance_maximo = 0
    
    for i in range(len(nums)):
        
        if i > alcance_maximo:
            return False
        
        alcance_maximo = max(alcance_maximo, i + nums[i])
        
        if alcance_maximo >= len(nums) - 1:
            return True
        
    return False
    
nums1 = [2,3,1,1,4]
nums2 = [3,2,1,0,4]

canJump(nums1)