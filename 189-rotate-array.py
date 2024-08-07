"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""

def rotate(nums, k):
    n = len(nums)
    # Se k > n. então, rodar o array k vezes, é o mesmo que rodar o array k % n vezes
    k = k % n
    # nums[:] -> Para criar uma cópia do array
    # nums[-k:] -> Vai selecionar os últimos k elementos do array
    # nums[:-k] -> Vai selecionar os primeiros n - k elementos do array z
    nums[:] = nums[-k:] + nums[:-k]

nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
rotate(nums1, k1)
print(nums1)