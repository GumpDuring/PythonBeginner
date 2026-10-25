class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = dict()
        for i,num in enumerate(nums):
            if target - num in hash:
                return [hash[target - num],i]
            hash[num] = i
        return[]

#用字典解决时间复杂度高的问题。（底层是哈希表，所有相关操作都是O(1)）。
