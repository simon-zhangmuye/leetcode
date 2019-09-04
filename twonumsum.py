# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/9/4 22:52'



def twoSum(nums, target):
    lens = len(nums)
    j=-1
    for i in range(1,lens):
        temp = nums[:i]
        if (target - nums[i]) in temp:
            j = temp.index(target - nums[i])
            break
    if j>=0:
        return [j,i]
