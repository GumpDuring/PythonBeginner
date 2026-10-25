class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = dict()
        for dex,i in enumerate(nums):
            if i in seen:
                return True
            seen[i] = dex
        return False
#或者用set