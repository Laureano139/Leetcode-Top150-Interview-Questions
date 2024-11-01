import random

class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.val_to_index = {}
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.nums)
        self.nums.append(val)
        return True
        
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.val_to_index:
            return False
        index = self.val_to_index[val]
        last_element = self.nums[-1]

        self.nums[index] = last_element
        self.val_to_index[last_element] = index
        self.nums.pop()
        del self.val_to_index[val]
        
        return True
    
    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.nums)
