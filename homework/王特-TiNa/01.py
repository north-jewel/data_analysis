# 给一个列表,里面有重复两次的元素,找到没有重复的元素
# input [ 2,2,1]
# output 1

def singleNumber(nums):
    dic = {}
    a = 0
    for num in nums:
        if num in dic:
            a = dic[num]+1
        else:
            a = 1
        dic[num] = a
    for key,val in dic.items():
        if val == 1:
            return key
nums = [4,1,2,1,2,3,2,3,1,2,3,4,1,2,3,4,6]
# print(singleNumber(nums))

def two(nums):
    nums2 = list(set(nums))
    for num in nums2:
        nums.remove(num)
        try:
            nums.remove(num)
        except:
            return num
# print(two(nums))

def teacher(nums):
    dic = {}
    for num in nums:
        if num in dic:
            dic.pop(num)
        else:
            dic[num] = 1
    return dic.popitem()[0]
print(teacher(nums))
