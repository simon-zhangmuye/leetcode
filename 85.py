# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/10/13 21:39'


# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = 2147483647
        res = target
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == target:
                    return s
                elif s < target:
                    if target - s < diff:
                        diff = target-s
                        res = s
                    left += 1
                    while left + 1 < right and nums[left] == nums[left-1]:
                        left+=1
                else:
                    if s - target < diff:
                        diff = s - target
                        res = s
                    right -= 1
                    while right-1>left and nums[right] == nums[right+1]:
                        right-=1
        return res
