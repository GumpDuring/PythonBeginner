class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j = 0,len(numbers)-1
        while True:
            sum = numbers[i] + numbers[j]
            if sum == target:
                back = [i+1,j+1]
                return back
            elif sum < target:
                i += 1
            elif sum > target:
                j -= 1