'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
'''

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # num_set = list(set(nums))*2
        # for i in nums:
        #     num_set.remove(i)
        # return num_set[0]
    
    
        # d = {}
        # # num_set = list(set(nums))
        # for x in nums:
        #     if x in d:
        #         d.pop(x)
        #     else:
        #         d[x] = 1
        # print(d)
        # return d.popitem()[0]
    
        # s = {}
        # for i in nums:
        #     if i in s.keys():
        #         s.pop(i)
        #     else:
        #         s[i]=1
        # return list(s.keys())[0]

    
        a = 0
        for num in nums:
            a = a ^ num
            print(num)
            print(a)
        return a     
