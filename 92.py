# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/10/16 15:07'


#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#   [7],
#   [2,2,3]
# ]
# 示例 2:
#
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dict = {}
        for i in range(1, target + 1):
            dict[i] = []

        for i in range(1, target + 1):
            for j in candidates:
                if i == j:
                    dict[i].append([i])
                elif i > j:
                    for k in dict[i - j]:
                        x = k[:]
                        x.append(j)
                        x.sort()  # 升序，便于后续去重
                        if x not in dict[i]:
                            dict[i].append(x)

        return dict[target]
