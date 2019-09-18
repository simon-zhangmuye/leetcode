# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/9/18 12:06'


# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


    def generate(self, numRows):
        """
        杨辉三角
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0: return []
        triangle = []
        for row in range(numRows):
            if row == 0:
                triangle.append([1])
            else:
                # row = 1, col = row + 1, c (0,1)
                tmp = [1]
                # 这里遍历range(row)是因为, 当前行的元素来自于前一行.
                for c in range(row):
                    # 当c == row-1时, 表示当前列为倒数第一个元素, 该元素与哨兵位置的0元素相加.
                    sum = (triangle[row-1][c] + 0) if (c == row-1) else (triangle[row-1][c]+triangle[row-1][c+1])
                    tmp.append(sum)
                triangle.append(tmp)
        return triangle
