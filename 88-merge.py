def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    
    # First I used the "slicing" technique to select the first m elements of each array
    nums1[:] = nums1[:m]
    nums2[:] = nums2[:n]

    # Then I used the "extend" method to add the elements of nums2 array to nums1 array
    nums1.extend(nums2)

    # Finally, I used the "sort" method to sort the elements of the final merged array
    nums1.sort()