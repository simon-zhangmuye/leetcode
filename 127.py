'''
-*- coding: utf-8 -*-
@Author  : Simon Zhang
@Time    : 2019/12/22 10:53
@Software: PyCharm
@File    : 127.py
'''


# 给你两个数组，arr1 和 arr2，
#
# arr2 中的元素各不相同
# arr2 中的每个元素都出现在 arr1 中
# 对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。
#
#  
#
# 示例：
#
# 输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# 输出：[2,2,2,1,4,3,3,9,6,7,19]
#  
#
# 提示：
#
# arr1.length, arr2.length <= 1000
# 0 <= arr1[i], arr2[i] <= 1000
# arr2 中的元素 arr2[i] 各不相同
# arr2 中的每个元素 arr2[i] 都出现在 arr1 中

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        out = []
        for n in arr1:
            a = False
            for j in arr2:
                if n == j:
                    a = True
            if not a:
                out.append(n)
        out.sort()
        #print(out)
        new = []
        for n in arr2:
            count = 0
            for j in arr1:
                if n == j:
                    count += 1
            if count > 0:
                for k in range(count):
                    new.append(n)
        for n in out:
            new.append(n)
        return new
