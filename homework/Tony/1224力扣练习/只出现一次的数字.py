class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = {}
        for num in nums:
            if num in a:
                a.pop(num)
            else:
                a[num] = 1
        return a.popitem()[0]

            
print(Solution().singleNumber(nums = [4,5,5,6,4,1,2,1,2]))
