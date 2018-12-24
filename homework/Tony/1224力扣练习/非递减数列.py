class Solution(object):
    def a(self,nums):
    #判断截断点，对截断点进行分析
        count=0
        n=0
        length=len(nums)
        for i in range(length-1):
            if nums[i]>nums[i+1]:
                count+=1
                n=i
        if count==0:#没有截断点
            return True
        if count>1:#截断点大于2 
            return False
        if count==1:#截断点为1，例如[1,2,3,9,5,8,12,13],
        #9和5之间产生一个截断点，
        #此时产生以下几种情况：
        #1.截断点在首位，截断点在倒数第二位，截断点产生峰值或谷值，返回True
        #2.否则为False
            if n==length-2 or n==0 or nums[n]<=nums[n+2] or nums[n-1]<=nums[n+1]:
                return True
            else:
                return False

x = Solution()
print(x.a(nums = [1,2,3,9,5,8,12,13]))
