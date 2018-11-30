class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list_1 = []
        
        for y in range(len(nums)):
            for i in nums:
                print(i[y])
                if i+i[y+1] == target:
                    list_1.append(i)
                    list_1.append(i[y+1])
                    return list_1
                else:
                    print('无匹配')
nums = [2, 7, 11, 15]
target = 9
a = Solution()
print(a.twoSum(nums, target))
