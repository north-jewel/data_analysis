'''
给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。

示例 1:

输入: [4,2,3]
输出: True
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
示例 2:

输入: [4,2,1]
输出: False
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
说明:  n 的范围为 [1, 10,000]。
'''

class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # count = 0
        # for i in range(1, len(nums)):
        #     if nums[i] < nums[i-1]:
        #         if count > 0:   
        #             return False
        #         if i > 1 and nums[i] < nums[i-2]:
        #             nums[i] = nums[i-1]
        #         count += 1
        # return True
    
        # change = 0
        # for i in range(len(nums)-1):
        #     if nums[i] > nums[i+1]:
        #         if i != 0 and nums[i-1] > nums[i+1]:
        #             nums[i+1] = nums[i] 
        #         change += 1
        #         if change > 1:
        #             return False 
        # return True 
        
#         [1,3,2,5,6]
#         [3,5,4,2,6,5]


#            [6,5,3,5,7]
#            [6,7,3,5,7]
            #     7
#            [4,2,1,4]
        
        n = 0
        for i in range(1,len(nums)):   #循环遍历整个数列
            if nums[i] < nums[i-1]:    #如果第1位置的元素小于它前一个元素(即第0位置的元素)，则：
                if n > 0:              #如果计数 大于 0 次：
                    return False       #则返回 FALSE
                if i >1 and nums[i] < nums[i-2]:      #如果此时的位置 大于 1(即最小从2起) 并且 第2位置的元素小于第0位置的元素，则：
                                                      #(表明前三个元素为递增或递减数列)
                    nums[i] = nums[i-1]               #将第1位置的元素赋值给第2位置
                                                      #这时第2位置的值等于第1位置的值
                n += 1                                #计数 加1
        return True                    #如果上述条件均未满足，则返回TRUE      
        
        
        #判断截断点，对截断点进行分析
#         count=0
#         n=0
#         length=len(nums)
#         for i in range(length-1):
#             if nums[i]>nums[i+1]:
#                 count+=1
#                 n=i
#         if count==0:#没有截断点
#             return True
#         if count>1:#截断点大于2 
#             return False
#         if count==1:#截断点为1，例如[1,2,3,9,5,8,12,13],
#         #9和5之间产生一个截断点，
#         #此时产生以下几种情况：
#         #1.截断点在首位，截断点在倒数第二位，截断点产生峰值或谷值，返回True
#         #2.否则为False
#             if n==length-2 or n==0 or nums[n]<=nums[n+2] or nums[n-1]<=nums[n+1]:
#                 return True
#             else:
#                 return False
        
        
        # count = 0
        # if len(nums)<=2:
        #     return True
        # for i in range(1,len(nums)):
        #     if nums[i]<nums[i-1]:
        #         if i==1:
        #             nums[i-1] = nums[i]
        #         else:
        #             if nums[i]>=nums[i-2]:
        #                 nums[i-1]=nums[i]
        #             elif nums[i]<nums[i-2]:
        #                 nums[i]=nums[i-1]
        #         count += 1
        #         break       
        # for j in range(i,len(nums)):
        #     if nums[j]<nums[j-1]:
        #         return False
        # return True
        
        
